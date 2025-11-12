package githubx

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"time"
)

// GetJSON fetches a JSON file via Contents API and decodes into out.
// When acceptRaw is true, it requests raw content and decodes JSON directly.
func GetJSON(r Repo, path, ref, token string, out any) error {
	if token == "" {
		return fmt.Errorf("missing token for private repo access")
	}
	u := fmt.Sprintf("https://api.github.com/repos/%s/%s/contents/%s?ref=%s", r.Owner, r.Name, path, ref)
	backoff := []time.Duration{0, 2 * time.Second, 4 * time.Second, 8 * time.Second}
	var lastErr error
	for i := 0; i < len(backoff); i++ {
		if i > 0 { time.Sleep(backoff[i]) }
		req, _ := http.NewRequest("GET", u, nil)
		req.Header.Set("User-Agent", "olaf-seed-tool")
		req.Header.Set("Authorization", "token "+token)
		req.Header.Set("Accept", "application/vnd.github.v3.raw")
		resp, err := http.DefaultClient.Do(req)
		if err != nil { lastErr = err; continue }
		defer resp.Body.Close()
		if resp.StatusCode >= 200 && resp.StatusCode < 300 {
			dec := json.NewDecoder(resp.Body)
			return dec.Decode(out)
		}
		// retry only on 5xx; treat others as final
		if resp.StatusCode < 500 { return fmt.Errorf("GET %s -> %d", u, resp.StatusCode) }
		lastErr = fmt.Errorf("GET %s -> %d", u, resp.StatusCode)
	}
	return lastErr
}

// GetRaw fetches raw bytes for a file via Contents API (using Accept: raw)
func GetRaw(r Repo, path, ref, token string) ([]byte, error) {
	if token == "" {
		return nil, fmt.Errorf("missing token")
	}
	u := fmt.Sprintf("https://api.github.com/repos/%s/%s/contents/%s?ref=%s", r.Owner, r.Name, path, ref)
	backoff := []time.Duration{0, 2 * time.Second, 4 * time.Second, 8 * time.Second}
	var lastErr error
	for i := 0; i < len(backoff); i++ {
		if i > 0 { time.Sleep(backoff[i]) }
		req, _ := http.NewRequest("GET", u, nil)
		req.Header.Set("User-Agent", "olaf-seed-tool")
		req.Header.Set("Authorization", "token "+token)
		req.Header.Set("Accept", "application/vnd.github.v3.raw")
		resp, err := http.DefaultClient.Do(req)
		if err != nil { lastErr = err; continue }
		defer resp.Body.Close()
		if resp.StatusCode >= 200 && resp.StatusCode < 300 {
			return io.ReadAll(resp.Body)
		}
		if resp.StatusCode < 500 { return nil, fmt.Errorf("GET %s -> %d", u, resp.StatusCode) }
		lastErr = fmt.Errorf("GET %s -> %d", u, resp.StatusCode)
	}
	return nil, lastErr
}

// ListDir lists directory entries via Contents API. Returns the API JSON array.
type DirEntry struct {
	Type        string `json:"type"`
	Name        string `json:"name"`
	Path        string `json:"path"`
	DownloadURL string `json:"download_url"`
	Content     string `json:"content"`
	Encoding    string `json:"encoding"`
}

func ListDir(r Repo, path, ref, token string) ([]DirEntry, error) {
	if token == "" {
		return nil, fmt.Errorf("missing token")
	}
	u := fmt.Sprintf("https://api.github.com/repos/%s/%s/contents/%s?ref=%s", r.Owner, r.Name, path, ref)
	backoff := []time.Duration{0, 2 * time.Second, 4 * time.Second, 8 * time.Second}
	var lastErr error
	for i := 0; i < len(backoff); i++ {
		if i > 0 { time.Sleep(backoff[i]) }
		req, _ := http.NewRequest("GET", u, nil)
		req.Header.Set("User-Agent", "olaf-seed-tool")
		req.Header.Set("Authorization", "token "+token)
		req.Header.Set("Accept", "application/vnd.github.v3+json")
		resp, err := http.DefaultClient.Do(req)
		if err != nil { lastErr = err; continue }
		defer resp.Body.Close()
		if resp.StatusCode >= 200 && resp.StatusCode < 300 {
			var out []DirEntry
			if err := json.NewDecoder(resp.Body).Decode(&out); err != nil { return nil, err }
			return out, nil
		}
		if resp.StatusCode < 500 { return nil, fmt.Errorf("GET %s -> %d", u, resp.StatusCode) }
		lastErr = fmt.Errorf("GET %s -> %d", u, resp.StatusCode)
	}
	return nil, lastErr
}

// DecodeBase64 helper for DirEntry.Content if type=="file" and encoding=="base64"
func DecodeBase64(s string) ([]byte, error) {
	return base64.StdEncoding.DecodeString(s)
}
