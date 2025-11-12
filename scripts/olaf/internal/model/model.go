package model

type RepoRef struct {
	URL    string
	Owner  string
	Repo   string
	Branch string // resolved main/master or API default
}

type Registry struct {
	SecondaryRepos []string `json:"secondary-repos"`
	UseOSS         bool     `json:"use-oss"`
}

type Collection struct {
	ID          string   `json:"id"`
	Name        string   `json:"name"`
	Description string   `json:"description"`
	Competencies []string `json:"competencies"`
}

type CollectionsFile struct {
	Collections []Collection `json:"collections"`
}
