package config

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"

	githubx "github.com/amadeus-xdlc/genai.olaf/scripts/olaf/internal/githubx"
)

const (
	RegistryRelPath    = "olaf-core/reference/olaf-registry.json"
	CollectionsRelPath = "olaf-core/reference/competency-collections.json"
	DefaultPrimarySeed = "https://github.com/Amadeus-xDLC/genai.olaf"
	DefaultOSS         = "https://github.com/AmadeusITGroup/olaf"
)

// Registry mirrors olaf-core/reference/olaf-registry.json
// { "secondary-repos": ["https://github.com/org/repo", ...], "use-oss": true }
// collection-only is dropped by design

type Registry struct {
	SecondaryRepos []string `json:"secondary-repos"`
	UseOSS         bool     `json:"use-oss"`
}

// LoadRegistry tries to fetch the registry from GitHub using the Contents API with token.
// If branch is empty, it attempts to resolve the default branch via API.
// This function only handles remote; callers may still apply local fallbacks.
func LoadRegistry(owner, repo, branch, token string) (*Registry, error) {
	if strings.TrimSpace(token) == "" {
		return nil, fmt.Errorf("missing token")
	}
	ref := strings.TrimSpace(branch)
	if ref == "" {
		b, err := githubx.DefaultBranch(githubx.Repo{Owner: owner, Name: repo}, token)
		if err == nil && b != "" {
			ref = b
		}
	}
	var reg Registry
	if err := githubx.GetJSON(githubx.Repo{Owner: owner, Name: repo}, RegistryRelPath, ref, token, &reg); err != nil {
		return nil, err
	}
	return &reg, nil
}

// LocalFallback loads a registry from local filesystem path if present.
func LocalFallback(rootedPath string) (*Registry, error) {
	var reg Registry
	b, err := os.ReadFile(rootedPath)
	if err != nil { return nil, err }
	if err := json.Unmarshal(b, &reg); err != nil { return nil, err }
	return &reg, nil
}
