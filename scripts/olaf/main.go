package main

import (
    "bufio"
	"encoding/json"
	"errors"
	"flag"
	"fmt"
	"io"
	"net/http"
	"os"
	"path"
	"path/filepath"
	"sort"
	"strings"
	"time"
	configx "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/config"
	collx "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/collections"
	githubx "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/githubx"
	model "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/model"
	syncx "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/syncer"
	uix "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/ui"
	util "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/util"
)

// Global GitHub token for helper functions (set in main)
var ghTokenGlobal string

// Build info; values can be overridden via -ldflags at build time
var (
    buildVersion = "0.0.1"
    buildCommit  = ""
    buildDate    = ""
)

// ts returns an RFC3339 timestamp for log lines
func ts() string { return time.Now().Format(time.RFC3339) }

func main() {
    // Support short alias -v for version before flag parsing
    for _, a := range os.Args[1:] {
        if a == "-v" {
            v := buildVersion
            if strings.TrimSpace(buildCommit) != "" { v += " (" + buildCommit + ")" }
            if strings.TrimSpace(buildDate) != "" { v += " built " + buildDate }
            fmt.Println(v)
            return
        }
    }
	versionFlag := flag.Bool("version", false, "Print version and exit")
	configPathFlag := flag.String("config", "", "Path to olaf-config.json")
	registryRepo := flag.String("registry-repo", configx.DefaultPrimarySeed, "Primary registry repository URL (overrides default)")
	ossURL := flag.String("oss-url", configx.DefaultOSS, "Fallback OSS GitHub repository URL (used if registry.use-oss=true)")
	branchFlag := flag.String("branch", "", "Git branch to use for the primary registry repo (requires --registry-repo)")
	selectFlag := flag.String("select", "", "Comma-separated collection IDs to select (non-interactive)")
	nonInteractive := flag.Bool("non-interactive", false, "Non-interactive mode (requires --select)")
	dryRun := flag.Bool("dry-run", false, "Do not modify local files; just print the plan")
	verbose := flag.Bool("verbose", false, "Verbose logging")
	tokenFlag := flag.String("token", "", "GitHub token (overrides GITHUB_TOKEN/GH_TOKEN)")
	remoteOnly := flag.Bool("remote-only", true, "Remote-only mode (default). Use --allow-local to enable local fallbacks")
	allowLocal := flag.Bool("allow-local", false, "Allow local fallbacks (overrides --remote-only)")
	multiFlag := flag.Bool("multi", false, "Install across multiple repos under current tree (interactive if multiple repos detected)")
	flag.Parse()

	// Handle --version early and exit
	if *versionFlag {
		v := buildVersion
		if strings.TrimSpace(buildCommit) != "" { v += " (" + buildCommit + ")" }
		if strings.TrimSpace(buildDate) != "" { v += " built " + buildDate }
		fmt.Println(v)
		return
	}

	// Resolve primary registry
	var effRegistry string
	var effBranch string
	var effOSS string
	{
		// Load config with precedence (CLI > config file). We probe config file paths after anchoring.
		type fileConfig struct {
			RegistryRepo string `json:"registry-repo"`
			Branch       string `json:"branch"`
			OSS          string `json:"oss-url"`
		}
		var cfg fileConfig
		// Determine config path: explicit flag first; else look in original and current working dirs
		// Note: cwd captured above; baseRoot may have been applied by now.
		var configPath string
		if strings.TrimSpace(*configPathFlag) != "" { configPath = strings.TrimSpace(*configPathFlag) }
		if configPath == "" {
			// try current dir
			cand := filepath.Join(".", "olaf-config.json")
			if _, err := os.Stat(cand); err == nil { configPath = cand }
		}
		if configPath != "" {
			if b, err := os.ReadFile(configPath); err == nil {
				_ = json.Unmarshal(b, &cfg)
			}
		}

		// Effective values with precedence: CLI > config > defaults
		effRegistry = strings.TrimSpace(*registryRepo)
		if effRegistry == "" && strings.TrimSpace(cfg.RegistryRepo) != "" { effRegistry = strings.TrimSpace(cfg.RegistryRepo) }
		effBranch = strings.TrimSpace(*branchFlag)
		if effBranch == "" && strings.TrimSpace(cfg.Branch) != "" { effBranch = strings.TrimSpace(cfg.Branch) }
		effOSS = strings.TrimSpace(*ossURL)
		if effOSS == "" && strings.TrimSpace(cfg.OSS) != "" { effOSS = strings.TrimSpace(cfg.OSS) }

		// Validate registry-repo if provided: must be http(s) GitHub URL
		if effRegistry != "" {
			if strings.HasPrefix(strings.ToLower(effRegistry), "http://") || strings.HasPrefix(strings.ToLower(effRegistry), "https://") {
				if _, err := util.ParseGitHubURL(effRegistry); err != nil {
					util.Fatal(fmt.Sprintf("invalid --registry-repo URL: %v", err))
				}
			} else {
				util.Fatal("--registry-repo must be an http(s) GitHub repo URL (local paths not yet supported)")
			}
		}
		if strings.TrimSpace(effBranch) != "" && strings.TrimSpace(effRegistry) == "" { util.Fatal("--branch requires --registry-repo") }
	}

	primary, err := util.ParseGitHubURL(effRegistry)
	util.MustNoErr(err)
	if strings.TrimSpace(effBranch) != "" { primary.Branch = strings.TrimSpace(effBranch) }

	if *verbose {
		fmt.Printf("Primary: %s/%s\n", primary.Owner, primary.Repo)
	}

	// Resolve auth token (flag > env)
	ghToken := util.ResolveToken(*tokenFlag)
	ghTokenGlobal = ghToken
	// Effective local usage (allow-local wins; remote-only=false also enables local for backward compatibility)
	useLocal := *allowLocal || !*remoteOnly
	if *verbose {
		tstate := "absent"
		if strings.TrimSpace(ghToken) != "" { tstate = "present" }
		fmt.Printf("[%s] [TRACE] flags: verbose=%v dry-run=%v remote-only=%v allow-local=%v non-interactive=%v\n", ts(), *verbose, *dryRun, *remoteOnly, *allowLocal, *nonInteractive)
		if strings.TrimSpace(effRegistry) != "" { fmt.Printf("[%s] [TRACE] registry-repo: %s\n", ts(), strings.TrimSpace(effRegistry)) }
		if strings.TrimSpace(effBranch) != "" { fmt.Printf("[%s] [TRACE] branch: %s\n", ts(), strings.TrimSpace(effBranch)) }
		fmt.Printf("[%s] [TRACE] token: %s\n", ts(), tstate)
	}

	// Anchor all relative paths to repository root (directory containing .git)
	cwd, _ := os.Getwd()
	baseRoot := cwd
	var gitPath string
	if p, ok := util.FindFileUpwards(".git", 12); ok {
		baseRoot = filepath.Dir(p)
		gitPath = p
		if *verbose { fmt.Printf("[%s] [TRACE] paths: found .git at %s -> baseRoot=%s\n", ts(), gitPath, baseRoot) }
	} else {
		if *verbose { fmt.Printf("[%s] [TRACE] paths: .git not found upwards from %s\n", ts(), cwd) }
		// Conservative fallback: if running in scripts/olaf, anchor two levels up
		scriptsOlaf := filepath.Join("scripts", "olaf")
		if strings.HasSuffix(strings.ReplaceAll(cwd, "\\", "/"), strings.ReplaceAll(scriptsOlaf, "\\", "/")) {
			baseRoot = filepath.Dir(filepath.Dir(cwd))
			if *verbose { fmt.Printf("[%s] [TRACE] paths: fallback anchor up2 from %s -> %s\n", ts(), cwd, baseRoot) }
		} else {
			// Try anchoring based on the executable's directory (commonly scripts/olaf)
			if exep, eerr := os.Executable(); eerr == nil {
				exedir := filepath.Dir(exep)
				cand := filepath.Dir(filepath.Dir(exedir))
				baseRoot = cand
				if *verbose { fmt.Printf("[%s] [TRACE] paths: fallback anchor via exe up2 from %s -> %s (exe=%s)\n", ts(), exedir, baseRoot, exep) }
			} else if *verbose {
				fmt.Printf("[%s] [TRACE] paths: unable to resolve repo root from %s (exe lookup failed: %v)\n", ts(), cwd, eerr)
			}
		}
	}
	if baseRoot == cwd {
		norm := strings.ReplaceAll(cwd, "\\", "/")
		if strings.Contains(norm, "/scripts/olaf") {
			cand := filepath.Dir(filepath.Dir(cwd))
			if _, err := os.Stat(filepath.Join(cand, ".git")); err == nil {
				if *verbose { fmt.Printf("[%s] [TRACE] paths: forced anchor via scripts/olaf -> %s\n", ts(), cand) }
				baseRoot = cand
			}
		}
	}
	if baseRoot != cwd {
		if *verbose { fmt.Printf("[%s] [TRACE] paths: anchoring to repo root: %s (was %s) [git=%s]\n", ts(), baseRoot, cwd, gitPath) }
		util.MustNoErr(os.Chdir(baseRoot))
	}
	if *verbose {
		if cur, err := os.Getwd(); err == nil {
			fmt.Printf("[%s] [TRACE] paths: cwd=%s\n", ts(), cur)
		}
	}

    // Multi-repo discovery (limit depth to 4)
    discoverGitRepos := func(root string, maxDepth int) []string {
        var repos []string
        rootAbs, _ := filepath.Abs(root)
        filepath.WalkDir(root, func(p string, d os.DirEntry, err error) error {
            if err != nil { return nil }
            // depth limit
            rel, _ := filepath.Rel(root, p)
            if rel != "." {
                depth := len(strings.Split(strings.ReplaceAll(rel, "\\", "/"), "/"))
                if depth > maxDepth { return filepath.SkipDir }
            }
            if d.IsDir() && strings.EqualFold(d.Name(), ".git") {
                repoRoot := filepath.Dir(p)
                // skip nested .git within .git
                if strings.Contains(strings.ReplaceAll(repoRoot, "\\", "/"), "/.git/") { return filepath.SkipDir }
                abs, _ := filepath.Abs(repoRoot)
                // avoid duplicates and ensure not the .git dir itself
                if abs != rootAbs {
                    repos = append(repos, abs)
                }
                return filepath.SkipDir
            }
            return nil
        })
        sort.Strings(repos)
        return repos
    }

    // Decide multi-mode
    multiMode := false
    targets := []string{}
    discovered := discoverGitRepos(baseRoot, 4)
    if *multiFlag {
        multiMode = true
        targets = discovered
    } else if len(discovered) > 0 && !*nonInteractive {
        fmt.Printf("Detected %d Git repos under %s. Enable multi-repo installation? [y/N]: ", len(discovered), baseRoot)
        reader := bufio.NewReader(os.Stdin)
        ans, _ := reader.ReadString('\n')
        ans = strings.TrimSpace(strings.ToLower(ans))
        if ans == "y" || ans == "yes" {
            multiMode = true
            targets = discovered
        }
    }

	// Parse OSS ref early for registry fallback
	ossRefParsed, _ := util.ParseGitHubURL(effOSS)
	// Load registry from primary, then OSS, then local (if allowed)
	registry, err := fetchRegistry(primary, ossRefParsed, ghToken, useLocal, *verbose)
	if err != nil {
		util.Fatal(fmt.Sprintf("registry resolution failed: tried primary %s and fallbacks (oss=%s, local=%v): %v", effRegistry, effOSS, useLocal, err))
	}

	// Build precedence: primary -> secondary (order) -> OSS (if enabled and not duplicate)
	repos := []model.RepoRef{primary}
	for _, r := range registry.SecondaryRepos {
		ref, perr := util.ParseGitHubURL(r)
		if perr != nil {
			if *verbose {
				fmt.Printf("[%s] [TRACE] skip secondary repo '%s': %v\n", ts(), r, perr)
			}
			continue
		}
		repos = append(repos, ref)
	}
	if registry.UseOSS {
		ossRef, oerr := util.ParseGitHubURL(*ossURL)
		if oerr == nil && !util.SameRepo(ossRef, primary) {
			repos = append(repos, ossRef)
		}
	}

	// Resolve branch for each repo (use API default when token present)
	for i := range repos {
		if strings.TrimSpace(repos[i].Branch) != "" {
			if *verbose { fmt.Printf("[%s] [TRACE] branch: %s/%s -> %s (preset)\n", ts(), repos[i].Owner, repos[i].Repo, repos[i].Branch) }
			continue
		}
		branch := ""
		method := ""
		if ghToken != "" {
			if b, derr := apiGetDefaultBranch(repos[i], ghToken); derr == nil && b != "" {
				branch = b
				method = "api"
			} else if *verbose {
				fmt.Printf("[%s] [TRACE] branch: %s/%s api miss: %v\n", ts(), repos[i].Owner, repos[i].Repo, derr)
			}
		}
		if branch == "" {
			branch = util.ResolveDefaultBranch(repos[i])
			if method == "" { method = "probe" }
		}
		repos[i].Branch = branch
		if *verbose { fmt.Printf("[%s] [TRACE] branch: %s/%s -> %s (%s)\n", ts(), repos[i].Owner, repos[i].Repo, branch, method) }
	}

	// Fetch collections with precedence (token-aware)
	localFallback := ""
	if useLocal {
		if p, ok := util.FindFileUpwards(configx.CollectionsRelPath, 6); ok {
			localFallback = p
		}
	}
	// map RepoRef -> collections.RepoRef for resolver
	crepos := make([]collx.RepoRef, 0, len(repos))
	for _, rr := range repos {
		crepos = append(crepos, collx.RepoRef{Owner: rr.Owner, Repo: rr.Repo, Branch: rr.Branch})
	}
	orderedC, byRepoC, err := collx.Resolve(crepos, ghToken, localFallback, *verbose, primary.Branch)
	if err != nil {
		util.Fatal(err.Error())
	}
	// Convert back to local types
	ordered := map[string]model.Collection{}
	byRepo := map[string]model.RepoRef{}
	for id, c := range orderedC {
		ordered[id] = model.Collection{ID: c.ID, Name: c.Name, Description: c.Description, Competencies: c.Competencies}
	}
	for id, r := range byRepoC {
		byRepo[id] = model.RepoRef{Owner: r.Owner, Repo: r.Repo, Branch: r.Branch}
	}
	if len(ordered) == 0 {
		util.Fatal("No collections discovered from any repo")
	}

	// Selection
	selected := []string{}
	if *nonInteractive {
		if strings.TrimSpace(*selectFlag) == "" {
			util.Fatal("--non-interactive requires --select with at least one collection ID or name")
		}
		for _, id := range uix.SplitCSV(*selectFlag) {
			id = strings.TrimSpace(id)
			found := false
			for cid, c := range ordered {
				if strings.ToLower(cid) == strings.ToLower(id) || strings.ToLower(c.Name) == strings.ToLower(id) {
					selected = append(selected, cid)
					found = true
					break
				}
			}
			if !found {
				util.Fatal(fmt.Sprintf("Unknown collection id or name: %s", id))
			}
		}
	} else {
		// convert to UI model
		orderedUI := map[string]uix.Collection{}
		for id, c := range ordered {
			orderedUI[id] = uix.Collection{ID: c.ID, Name: c.Name}
		}
		selected = uix.PromptSelect(orderedUI)
	}
	if len(selected) == 0 {
		util.Fatal("You must select at least one collection")
	}

	// Plan
	fmt.Println("\nPlan:")
	for _, id := range selected {
		src := byRepo[id]
		fmt.Printf("- %s from %s/%s (%s)\n", id, src.Owner, src.Repo, src.Branch)
	}
    if multiMode {
        fmt.Println("\nTargets:")
        for _, rp := range targets {
            status := "install"
            if _, err := os.Stat(filepath.Join(rp, ".olaf")); err == nil { status = "skip (.olaf present)" }
            fmt.Printf("- %s [%s]\n", rp, status)
        }
    }

	if *dryRun {
		fmt.Println("\nDry-run mode: skipping downloads and local updates.")
		return
	}

	// Downloads and local updates (atomic via cache-then-swap)
	// 1) Prepare tmp dirs
	tmpRef := filepath.Join(".olaf", ".tmp-reference")
	tmpComps := filepath.Join(".olaf", ".tmp-competencies")
	_ = os.RemoveAll(tmpRef)
	_ = os.RemoveAll(tmpComps)
	util.MustNoErr(os.MkdirAll(tmpRef, 0o755))
	util.MustNoErr(os.MkdirAll(tmpComps, 0o755))
	// Ensure cleanup on exit (best-effort)
	defer os.RemoveAll(tmpRef)
	defer os.RemoveAll(tmpComps)
	util.MustNoErr(os.MkdirAll(".github/prompts", 0o755))
	util.MustNoErr(os.MkdirAll(".windsurf/workflows", 0o755))
	if *verbose {
		aref, _ := filepath.Abs(filepath.Join(".olaf", "olaf-core", "reference"))
		acomps, _ := filepath.Abs(filepath.Join(".olaf", "olaf-core", "competencies"))
		atmpRef, _ := filepath.Abs(tmpRef)
		atmpComps, _ := filepath.Abs(tmpComps)
		fmt.Printf("[%s] [TRACE] paths: tmpRef=%s tmpComps=%s\n", ts(), atmpRef, atmpComps)
		fmt.Printf("[%s] [TRACE] paths: finalRef=%s finalComps=%s\n", ts(), aref, acomps)
	}

	// 2) Copy reference from primary repo into tmp
	fmt.Println("\nDownloading reference from primary repo → .olaf/.tmp-reference …")
	util.MustNoErr(syncx.DownloadDir(syncx.Repo{Owner: primary.Owner, Name: primary.Repo, Branch: primary.Branch}, "olaf-core/reference", tmpRef, ghTokenGlobal))

	// 2b) Adapt collections to only the user-selected ones and remove registry from tmpRef
	{
		// Build filtered collections payload
		type coll struct {
			ID           string   `json:"id"`
			Name         string   `json:"name"`
			Description  string   `json:"description"`
			Competencies []string `json:"competencies"`
		}
		payload := struct{ Collections []coll `json:"collections"` }{Collections: []coll{}}
		for _, id := range selected {
			c := ordered[id]
			payload.Collections = append(payload.Collections, coll{ID: c.ID, Name: c.Name, Description: c.Description, Competencies: c.Competencies})
		}
		b, merr := json.MarshalIndent(payload, "", "  ")
		util.MustNoErr(merr)
		util.MustNoErr(syncx.WriteFileAtomic(filepath.Join(tmpRef, "competency-collections.json"), b))
		_ = os.Remove(filepath.Join(tmpRef, "olaf-registry.json"))
		if *verbose {
			ap1, _ := filepath.Abs(filepath.Join(tmpRef, "competency-collections.json"))
			fmt.Printf("[%s] [TRACE] collections: filtered -> %s (count=%d)\n", ts(), ap1, len(payload.Collections))
			ap2, _ := filepath.Abs(filepath.Join(tmpRef, "olaf-registry.json"))
			fmt.Printf("[%s] [TRACE] registry: removed from TMP if present -> %s\n", ts(), ap2)
		}
	}

	// 3) For each selected collection, copy competencies from its source repo into tmp
	// De-duplicate competencies across multiple collections
	compSet := map[string]bool{}
	for _, id := range selected {
		coll := ordered[id]
		srcRepo := byRepo[id]
		for _, comp := range coll.Competencies {
			if compSet[comp] { continue }
			compSet[comp] = true
			dst := filepath.Join(tmpComps, comp)
			srcPath := path.Join("olaf-core/competencies", comp)
			fmt.Printf("- Download competency %s from %s/%s → %s\n", comp, srcRepo.Owner, srcRepo.Repo, dst)
			util.MustNoErr(syncx.DownloadDir(syncx.Repo{Owner: srcRepo.Owner, Name: srcRepo.Repo, Branch: srcRepo.Branch}, srcPath, dst, ghTokenGlobal))
		}
	}

    // 4) Generate query-competency index from downloaded manifests in TMP (atomic)
    fmt.Println("\nGenerating query-competency-index.md …")
    compIDs := make([]string, 0, len(compSet))
    for id := range compSet {
        compIDs = append(compIDs, id)
    }
    sort.Strings(compIDs)
    idxContent, err := syncx.GenerateIndexFrom(compIDs, "custom", tmpComps)
    util.MustNoErr(err)
    util.MustNoErr(os.WriteFile(filepath.Join(tmpRef, "query-competency-index.md"), []byte(idxContent), 0o644))
    if *verbose {
        ap, _ := filepath.Abs(filepath.Join(tmpRef, "query-competency-index.md"))
        fmt.Printf("[%s] [TRACE] index: written to TMP %s\n", ts(), ap)
    }

    // 5) Atomically swap tmp dirs into place
    if !multiMode {
        util.MustNoErr(syncx.ReplaceDirAtomic(tmpRef, filepath.Join(".olaf", "olaf-core", "reference")))
        util.MustNoErr(syncx.ReplaceDirAtomic(tmpComps, filepath.Join(".olaf", "olaf-core", "competencies")))
        fmt.Println("✓ index written at .olaf/olaf-core/reference/query-competency-index.md")
    }

    if !multiMode {
        // 6) Refresh /olaf-* commands in .github/prompts and .windsurf/workflows (atomic)
        fmt.Println("\nRefreshing /olaf-* command files …")
        util.MustNoErr(syncx.RefreshCommandsAtomic(compIDs))

        // 7) Update Copilot instructions (prepend first line from primary repo)
        fmt.Println("\nUpdating Copilot instructions …")
        util.MustNoErr(syncx.UpdateCopilot(syncx.Repo{Owner: primary.Owner, Name: primary.Repo, Branch: primary.Branch}, ghTokenGlobal, *verbose))

        // 8) Replace bootstrap-olaf.md/olaf-bootstrap.md in Windsurf rules and Kiro steering from primary (best-effort)
        fmt.Println("\nSyncing bootstrap-olaf.md …")
        util.MustNoErr(syncx.SyncBootstrap(syncx.Repo{Owner: primary.Owner, Name: primary.Repo, Branch: primary.Branch}, ghTokenGlobal, *verbose))

        // 9) Sync whitelisted scripts from olaf-script.json (best-effort, atomic writes)
        fmt.Println("\nSyncing scripts from olaf-script.json …")
        util.MustNoErr(syncx.SyncScripts(syncx.Repo{Owner: primary.Owner, Name: primary.Repo, Branch: primary.Branch}, ghTokenGlobal))

        // 10) Ensure .git/info/exclude contains required patterns
        fmt.Println("\nEnsuring .git/info/exclude …")
        util.MustNoErr(syncx.EnsureGitExclude())

        fmt.Println("\nDone.")
    } else {
        // Multi-repo: write to global cache and replicate
        home, _ := os.UserHomeDir()
        globalRoot := filepath.Join(home, ".olaf-global")
        fmt.Printf("\nUpdating global cache at %s …\n", globalRoot)
        util.MustNoErr(syncx.ReplaceDirAtomic(tmpRef, filepath.Join(globalRoot, "olaf-core", "reference")))
        util.MustNoErr(syncx.ReplaceDirAtomic(tmpComps, filepath.Join(globalRoot, "olaf-core", "competencies")))
        // replicate to targets
        for _, rp := range targets {
            if _, err := os.Stat(filepath.Join(rp, ".olaf")); err == nil {
                fmt.Printf("- Skip %s (.olaf present)\n", rp)
                continue
            }
            fmt.Printf("- Installing to %s …\n", rp)
            // copy olaf-core
            util.MustNoErr(syncx.CopyDir(filepath.Join(globalRoot, "olaf-core"), filepath.Join(rp, ".olaf", "olaf-core")))
            // ensure dirs
            util.MustNoErr(os.MkdirAll(filepath.Join(rp, ".github", "prompts"), 0o755))
            util.MustNoErr(os.MkdirAll(filepath.Join(rp, ".windsurf", "workflows"), 0o755))
            // Run repo-local updates by temporarily chdir
            cur, _ := os.Getwd()
            _ = os.Chdir(rp)
            util.MustNoErr(syncx.RefreshCommandsAtomic(compIDs))
            util.MustNoErr(syncx.UpdateCopilot(syncx.Repo{Owner: primary.Owner, Name: primary.Repo, Branch: primary.Branch}, ghTokenGlobal, *verbose))
            util.MustNoErr(syncx.SyncBootstrap(syncx.Repo{Owner: primary.Owner, Name: primary.Repo, Branch: primary.Branch}, ghTokenGlobal, *verbose))
            util.MustNoErr(syncx.SyncScripts(syncx.Repo{Owner: primary.Owner, Name: primary.Repo, Branch: primary.Branch}, ghTokenGlobal))
            util.MustNoErr(syncx.EnsureGitExclude())
            _ = os.Chdir(cur)
        }
        fmt.Println("\nDone.")
    }
}

func fetchRegistry(primary model.RepoRef, oss model.RepoRef, token string, allowLocal bool, verbose bool) (*model.Registry, error) {
    // PRIMARY via API
    if strings.TrimSpace(token) != "" {
        if verbose { fmt.Printf("[%s] [TRACE] registry: API %s/%s@%s path=%s\n", ts(), primary.Owner, primary.Repo, primary.Branch, configx.RegistryRelPath) }
        if reg, err := configx.LoadRegistry(primary.Owner, primary.Repo, primary.Branch, token); err == nil {
            if verbose {
                if b, e2 := githubx.GetRaw(githubx.Repo{Owner: primary.Owner, Name: primary.Repo}, configx.RegistryRelPath, primary.Branch, token); e2 == nil {
                    fmt.Printf("[%s] [TRACE] registry: API OK %s/%s@%s (size=%d bytes)\n", ts(), primary.Owner, primary.Repo, primary.Branch, len(b))
                } else {
                    fmt.Printf("[%s] [TRACE] registry: API OK %s/%s@%s\n", ts(), primary.Owner, primary.Repo, primary.Branch)
                }
            }
            return &model.Registry{SecondaryRepos: reg.SecondaryRepos, UseOSS: reg.UseOSS}, nil
        } else if verbose {
            fmt.Printf("[%s] [TRACE] registry: API miss %s/%s@%s (%v)\n", ts(), primary.Owner, primary.Repo, primary.Branch, err)
        }
    }
    // PRIMARY via RAW
    for _, br := range []string{primary.Branch, "distribution", "main", "master"} {
        if br == "" { continue }
        u := util.RawURL(primary, br, configx.RegistryRelPath)
        if verbose { fmt.Printf("[%s] [TRACE] registry: RAW %s\n", ts(), u) }
        var reg model.Registry
        if err := util.FetchJSON(u, &reg); err == nil {
            if verbose {
                if resp, e2 := http.Get(u); e2 == nil {
                    defer resp.Body.Close()
                    if resp.StatusCode >= 200 && resp.StatusCode < 300 {
                        if b, e3 := io.ReadAll(resp.Body); e3 == nil { fmt.Printf("[%s] [TRACE] registry: RAW OK %s (size=%d bytes)\n", ts(), u, len(b)) } else { fmt.Printf("[%s] [TRACE] registry: RAW OK %s\n", ts(), u) }
                    } else { fmt.Printf("[%s] [TRACE] registry: RAW OK %s\n", ts(), u) }
                } else { fmt.Printf("[%s] [TRACE] registry: RAW OK %s\n", ts(), u) }
            }
            return &reg, nil
        } else if verbose {
            if resp, e2 := http.Get(u); e2 == nil {
                defer resp.Body.Close()
                fmt.Printf("[%s] [TRACE] registry: RAW miss %s -> %d\n", ts(), u, resp.StatusCode)
            } else {
                fmt.Printf("[%s] [TRACE] registry: RAW miss %s (%v)\n", ts(), u, e2)
            }
        }
    }
    // OSS via API
    if verbose { fmt.Printf("[%s] [TRACE] registry: trying OSS fallback %s/%s\n", ts(), oss.Owner, oss.Repo) }
    if strings.TrimSpace(token) != "" {
        if verbose { fmt.Printf("[%s] [TRACE] registry: API %s/%s@%s path=%s\n", ts(), oss.Owner, oss.Repo, oss.Branch, configx.RegistryRelPath) }
        if reg, err := configx.LoadRegistry(oss.Owner, oss.Repo, oss.Branch, token); err == nil {
            if verbose {
                if b, e2 := githubx.GetRaw(githubx.Repo{Owner: oss.Owner, Name: oss.Repo}, configx.RegistryRelPath, oss.Branch, token); e2 == nil {
                    fmt.Printf("[%s] [TRACE] registry: API OK %s/%s@%s (size=%d bytes)\n", ts(), oss.Owner, oss.Repo, oss.Branch, len(b))
                } else {
                    fmt.Printf("[%s] [TRACE] registry: API OK %s/%s@%s\n", ts(), oss.Owner, oss.Repo, oss.Branch)
                }
            }
            return &model.Registry{SecondaryRepos: reg.SecondaryRepos, UseOSS: reg.UseOSS}, nil
        } else if verbose {
            fmt.Printf("[%s] [TRACE] registry: API miss %s/%s@%s (%v)\n", ts(), oss.Owner, oss.Repo, oss.Branch, err)
        }
    }
    // OSS via RAW
    for _, br := range []string{oss.Branch, "distribution", "main", "master"} {
        if br == "" { continue }
        u := util.RawURL(oss, br, configx.RegistryRelPath)
        if verbose { fmt.Printf("[trace] registry: RAW %s\n", u) }
        var reg model.Registry
        if err := util.FetchJSON(u, &reg); err == nil {
            if verbose {
                if resp, e2 := http.Get(u); e2 == nil {
                    defer resp.Body.Close()
                    if resp.StatusCode >= 200 && resp.StatusCode < 300 {
                        if b, e3 := io.ReadAll(resp.Body); e3 == nil { fmt.Printf("[trace] registry: RAW OK %s (size=%d bytes)\n", u, len(b)) } else { fmt.Printf("[trace] registry: RAW OK %s\n", u) }
                    } else { fmt.Printf("[trace] registry: RAW OK %s\n", u) }
                } else { fmt.Printf("[trace] registry: RAW OK %s\n", u) }
            }
            return &reg, nil
        } else if verbose {
            if resp, e2 := http.Get(u); e2 == nil {
                defer resp.Body.Close()
                fmt.Printf("[trace] registry: RAW miss %s -> %d\n", u, resp.StatusCode)
            } else {
                fmt.Printf("[trace] registry: RAW miss %s (%v)\n", u, e2)
            }
        }
    }
    // LOCAL
    if allowLocal {
        if p, ok := util.FindFileUpwards(configx.RegistryRelPath, 6); ok {
            if verbose { fmt.Printf("[%s] [TRACE] registry: LOCAL %s\n", ts(), p) }
            var reg model.Registry
            if b, err := os.ReadFile(p); err == nil {
                if e := json.Unmarshal(b, &reg); e == nil {
                    if verbose { fmt.Printf("[%s] [TRACE] registry: LOCAL OK %s\n", ts(), p) }
                    return &reg, nil
                } else if verbose {
                    fmt.Printf("[%s] [TRACE] registry: LOCAL miss %s (invalid JSON)\n", ts(), p)
                }
            } else if verbose {
                fmt.Printf("[%s] [TRACE] registry: LOCAL miss %s (read error: %v)\n", ts(), p, err)
            }
        }
    }
    return nil, errors.New("registry not found")
}

func apiGetDefaultBranch(r model.RepoRef, token string) (string, error) {
    if strings.TrimSpace(token) == "" {
        return "", errors.New("no token")
    }
    u := fmt.Sprintf("https://api.github.com/repos/%s/%s", r.Owner, r.Repo)
    req, _ := http.NewRequest("GET", u, nil)
    req.Header.Set("Accept", "application/vnd.github.v3+json")
    req.Header.Set("User-Agent", "olaf-seed-tool")
    req.Header.Set("Authorization", "token "+token)
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()
	if resp.StatusCode < 200 || resp.StatusCode >= 300 {
		return "", fmt.Errorf("GET %s -> %d", u, resp.StatusCode)
	}
	var dv struct{ DefaultBranch string `json:"default_branch"` }
	if err := json.NewDecoder(resp.Body).Decode(&dv); err != nil {
		return "", err
	}
	return strings.TrimSpace(dv.DefaultBranch), nil
}
