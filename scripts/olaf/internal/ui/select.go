package ui

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

type Collection struct {
	ID   string
	Name string
}

// PromptSelect prints a list of collections and returns selected IDs from user input
func PromptSelect(ordered map[string]Collection) []string {
	fmt.Println("Available collections (first source wins; ordered by source precedence, then name):")
	ids := make([]string, 0, len(ordered))
	for id := range ordered { ids = append(ids, id) }
	sort.Strings(ids)
	for i, id := range ids {
		c := ordered[id]
		fmt.Printf("  [%d] %s (%s)\n", i+1, c.Name, c.ID)
	}
	fmt.Println()
	fmt.Println("Enter one or more numbers or IDs, comma-separated (e.g., 1,3 or core,developer):")
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("> ")
	if !scanner.Scan() { return nil }
	line := strings.TrimSpace(scanner.Text())
	if line == "" { return nil }
	chosen := map[string]bool{}
	for _, tok := range SplitCSV(line) {
		if isDigits(tok) {
			idx := atoi(tok) - 1
			if idx >= 0 && idx < len(ids) { chosen[ids[idx]] = true }
			continue
		}
		if _, ok := ordered[tok]; ok { chosen[tok] = true }
	}
	out := make([]string, 0, len(chosen))
	for id := range chosen { out = append(out, id) }
	sort.Strings(out)
	return out
}

func SplitCSV(s string) []string {
	parts := strings.Split(s, ",")
	res := make([]string, 0, len(parts))
	for _, p := range parts {
		p = strings.TrimSpace(p)
		if p != "" { res = append(res, p) }
	}
	return res
}

func isDigits(s string) bool {
	for _, r := range s { if r < '0' || r > '9' { return false } }
	return s != ""
}

func atoi(s string) int {
	var n int
	for _, r := range s { n = n*10 + int(r-'0') }
	return n
}
