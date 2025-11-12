package collections

import (
    "encoding/json"
    "fmt"
    "os"
    "strings"
)

// RepoRef is a minimal repo reference for precedence resolution
 type RepoRef struct {
	Owner  string
	Repo   string
	Branch string
}

// Resolve applies precedence across repos (first wins) and returns selected collections and their source repo.
// If preferredBranch is provided, try that branch first for each repo, then the repo's resolved branch.
func Resolve(repos []RepoRef, token string, localFallbackPath string, verbose bool, preferredBranch string) (map[string]Collection, map[string]RepoRef, error) {
	result := map[string]Collection{}
	byRepo := map[string]RepoRef{}
	// Try remote for each repo first (no local fallback here)
	for _, rr := range repos {
		tried := false
		// Build branch attempt order
		attempts := []string{}
		if strings.TrimSpace(preferredBranch) != "" { attempts = append(attempts, preferredBranch) }
		if strings.TrimSpace(rr.Branch) != "" && rr.Branch != preferredBranch { attempts = append(attempts, rr.Branch) }
		if len(attempts) == 0 { attempts = []string{""} }
		var cf *CollectionsFile
		var err error
		var usedBranch string
		for _, br := range attempts {
			tried = true
			cf, err = FetchCollectionsForRepo(rr.Owner, rr.Repo, br, token, "", verbose)
			if err == nil { usedBranch = br; break }
		}
		if err != nil {
			if verbose {
				if tried {
					fmt.Printf("[trace] collections: skip %s/%s (branches tried: %v): %v\n", rr.Owner, rr.Repo, attempts, err)
				} else {
					fmt.Printf("[trace] collections: skip %s/%s: %v\n", rr.Owner, rr.Repo, err)
				}
			}
			continue
		}
		for _, c := range cf.Collections {
			if _, exists := result[c.ID]; exists {
				continue
			}
			result[c.ID] = c
			byRepo[c.ID] = RepoRef{Owner: rr.Owner, Repo: rr.Repo, Branch: usedBranch}
		}
	}
	if len(result) > 0 {
		return result, byRepo, nil
	}
	// If nothing found remotely, use local fallback if provided
	if strings.TrimSpace(localFallbackPath) != "" {
		if verbose {
			fmt.Printf("[trace] collections: FINAL LOCAL %s\n", localFallbackPath)
		}
		if b, err := os.ReadFile(localFallbackPath); err == nil {
			var cf CollectionsFile
			if e := json.Unmarshal(b, &cf); e == nil {
				for _, c := range cf.Collections {
					if _, exists := result[c.ID]; exists {
						continue
					}
					result[c.ID] = c
					byRepo[c.ID] = RepoRef{Owner: "local", Repo: "fallback", Branch: ""}
				}
				if len(result) > 0 {
					return result, byRepo, nil
				}
			} else if verbose {
				fmt.Printf("[trace] collections: FINAL LOCAL miss %s (invalid JSON)\n", localFallbackPath)
			}
		} else if verbose {
			fmt.Printf("[trace] collections: FINAL LOCAL miss %s (read error: %v)\n", localFallbackPath, err)
		}
	}
	return nil, nil, fmt.Errorf("no collections discovered")
}
