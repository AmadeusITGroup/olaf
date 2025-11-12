package collections

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"

	githubx "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/githubx"
)

const collectionsRelPath = "olaf-core/reference/competency-collections.json"

// Collection and CollectionsFile mirror the schema used by olaf
// We duplicate lightweight structs here to avoid circular deps.

type Collection struct {
	ID           string   `json:"id"`
	Name         string   `json:"name"`
	Description  string   `json:"description"`
	Competencies []string `json:"competencies"`
}

type CollectionsFile struct {
	Collections []Collection `json:"collections"`
}

// FetchCollectionsForRepo tries token-auth Contents API, then raw URL, then local fallback path.
// localFallbackPath is optional; if provided and remote fails, it will be read from disk.
func FetchCollectionsForRepo(owner, repo, branch, token, localFallbackPath string, verbose bool) (*CollectionsFile, error) {
	if strings.TrimSpace(token) != "" {
		if verbose {
			fmt.Printf("[trace] collections: API %s/%s@%s path=%s\n", owner, repo, branch, collectionsRelPath)
		}
		var cf CollectionsFile
		if err := githubx.GetJSON(githubx.Repo{Owner: owner, Name: repo}, collectionsRelPath, branch, token, &cf); err == nil {
			if verbose {
				if b, e2 := githubx.GetRaw(githubx.Repo{Owner: owner, Name: repo}, collectionsRelPath, branch, token); e2 == nil {
					fmt.Printf("[trace] collections: API OK %s/%s@%s (size=%d bytes)\n", owner, repo, branch, len(b))
				} else {
					fmt.Printf("[trace] collections: API OK %s/%s@%s\n", owner, repo, branch)
				}
			}
			return &cf, nil
		} else if verbose {
			fmt.Printf("[trace] collections: API miss %s/%s@%s (%v)\n", owner, repo, branch, err)
		}
	}
	// Raw public path fallback
	raw := fmt.Sprintf("https://raw.githubusercontent.com/%s/%s/%s/%s", owner, repo, branch, collectionsRelPath)
	if verbose {
		fmt.Printf("[trace] collections: RAW %s\n", raw)
	}
	if r, err := http.Get(raw); err == nil {
		defer r.Body.Close()
		if r.StatusCode >= 200 && r.StatusCode < 300 {
			b, _ := io.ReadAll(r.Body)
			var cf CollectionsFile
			if json.Unmarshal(b, &cf) == nil {
				if verbose {
					fmt.Printf("[trace] collections: RAW OK %s (size=%d bytes)\n", raw, len(b))
				}
				return &cf, nil
			} else if verbose {
				fmt.Printf("[trace] collections: RAW miss %s (invalid JSON)\n", raw)
			}
		} else if verbose {
			fmt.Printf("[trace] collections: RAW miss %s -> %d\n", raw, r.StatusCode)
		}
	} else if verbose {
		fmt.Printf("[trace] collections: RAW miss %s (%v)\n", raw, err)
	}
	// Local fallback if provided
	if strings.TrimSpace(localFallbackPath) != "" {
		if verbose {
			fmt.Printf("[trace] collections: LOCAL %s\n", localFallbackPath)
		}
		b, err := os.ReadFile(localFallbackPath)
		if err == nil {
			var cf CollectionsFile
			if json.Unmarshal(b, &cf) == nil {
				if verbose {
					fmt.Printf("[trace] collections: LOCAL OK %s (size=%d bytes)\n", localFallbackPath, len(b))
				}
				return &cf, nil
			} else if verbose {
				fmt.Printf("[trace] collections: LOCAL miss %s (invalid JSON)\n", localFallbackPath)
			}
		} else if verbose {
			fmt.Printf("[trace] collections: LOCAL miss %s (read error: %v)\n", localFallbackPath, err)
		}
	}
	return nil, fmt.Errorf("collections not found for %s/%s@%s (tried token/raw/local)", owner, repo, branch)
}
