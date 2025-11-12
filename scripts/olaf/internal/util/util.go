package util

import (
	"encoding/json"
	"fmt"
	"net/http"
	"path"
	"path/filepath"
	"strings"
    "os"

	model "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/model"
)

// ParseGitHubURL parses https://github.com/{owner}/{repo}[.git][@branch]
// Also supports short format: {owner}/{repo}[@branch]
func ParseGitHubURL(raw string) (model.RepoRef, error) {
	// Extract branch if present (format: url@branch or owner/repo@branch)
	branch := ""
	repoURL := raw
	if atIdx := strings.LastIndex(raw, "@"); atIdx != -1 {
		branch = strings.TrimSpace(raw[atIdx+1:])
		repoURL = raw[:atIdx]
	}

	// Handle short format: owner/repo
	if !strings.HasPrefix(repoURL, "https://") && !strings.HasPrefix(repoURL, "http://") {
		parts := strings.SplitN(repoURL, "/", 3)
		if len(parts) < 2 {
			return model.RepoRef{}, fmt.Errorf("unsupported GitHub URL: %s", raw)
		}
		owner := parts[0]
		repo := strings.TrimSuffix(parts[1], ".git")
		fullURL := fmt.Sprintf("https://github.com/%s/%s", owner, repo)
		return model.RepoRef{URL: fullURL, Owner: owner, Repo: repo, Branch: branch}, nil
	}

	// Handle full URL format: https://github.com/owner/repo
	const p = "https://github.com/"
	if !strings.HasPrefix(repoURL, p) {
		return model.RepoRef{}, fmt.Errorf("unsupported GitHub URL: %s", raw)
	}
	rest := strings.TrimPrefix(repoURL, p)
	parts := strings.SplitN(rest, "/", 3)
	if len(parts) < 2 {
		return model.RepoRef{}, fmt.Errorf("unsupported GitHub URL: %s", raw)
	}
	owner := parts[0]
	repo := strings.TrimSuffix(parts[1], ".git")
	return model.RepoRef{URL: repoURL, Owner: owner, Repo: repo, Branch: branch}, nil
}

// RawURL builds a raw.githubusercontent.com URL for a repo path at a branch
func RawURL(r model.RepoRef, branch, pth string) string {
	pth = path.Clean(pth)
	return fmt.Sprintf("https://raw.githubusercontent.com/%s/%s/%s/%s", r.Owner, r.Repo, branch, pth)
}

// URLExists performs a HEAD request and returns true when 2xx
func URLExists(u string) bool {
	resp, err := http.Head(u)
	if err != nil { return false }
	defer resp.Body.Close()
	return resp.StatusCode >= 200 && resp.StatusCode < 300
}

// FetchJSON GETs a JSON URL into out
func FetchJSON[T any](u string, out *T) error {
	resp, err := http.Get(u)
	if err != nil { return err }
	defer resp.Body.Close()
	if resp.StatusCode < 200 || resp.StatusCode >= 300 { return fmt.Errorf("GET %s -> %d", u, resp.StatusCode) }
	dec := json.NewDecoder(resp.Body)
	return dec.Decode(out)
}

// ResolveDefaultBranch probes main/master via raw URL fallbacks
func ResolveDefaultBranch(r model.RepoRef) string {
	for _, br := range []string{"main", "master"} {
		if URLExists(RawURL(r, br, "olaf-core/reference/competency-collections.json")) {
			return br
		}
	}
	return "main"
}

// Convenience helpers used by main
func MustNoErr(err error) {
    if err != nil { Fatal(err.Error()) }
}

func Fatal(msg string) {
    fmt.Fprintln(os.Stderr, "Error:", msg)
    os.Exit(1)
}

func ResolveToken(flagVal string) string {
    if strings.TrimSpace(flagVal) != "" { return flagVal }
    if v := strings.TrimSpace(os.Getenv("GITHUB_TOKEN")); v != "" { return v }
    if v := strings.TrimSpace(os.Getenv("GH_TOKEN")); v != "" { return v }
    return ""
}

func SameRepo(a, b model.RepoRef) bool { return a.Owner == b.Owner && a.Repo == b.Repo }

func FindFileUpwards(relPath string, maxUpLevels int) (string, bool) {
    cwd, _ := os.Getwd()
    for i := 0; i <= maxUpLevels; i++ {
        p := filepath.Join(cwd, relPath)
        // Consider both files and directories as a hit. This lets callers search for ".git" (a directory)
        if _, err := os.Stat(p); err == nil { return p, true }
        parent := filepath.Dir(cwd)
        if parent == cwd || parent == "." || parent == "" { break }
        cwd = parent
    }
    return "", false
}
