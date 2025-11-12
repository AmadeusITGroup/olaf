package githubx

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"os"
	"strings"
)

// Repo identifies a GitHub repository (branch is resolved separately)
type Repo struct {
	Owner string
	Name  string
}

// ResolveToken returns the GitHub token from flag or common env vars
func ResolveToken(flagVal string) string {
	if strings.TrimSpace(flagVal) != "" {
		return flagVal
	}
	if v := strings.TrimSpace(os.Getenv("GITHUB_TOKEN")); v != "" {
		return v
	}
	if v := strings.TrimSpace(os.Getenv("GH_TOKEN")); v != "" {
		return v
	}
	return ""
}

// DefaultBranch fetches the default branch via GitHub API
func DefaultBranch(r Repo, token string) (string, error) {
	if strings.TrimSpace(token) == "" {
		return "", errors.New("no token")
	}
	u := fmt.Sprintf("https://api.github.com/repos/%s/%s", r.Owner, r.Name)
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
