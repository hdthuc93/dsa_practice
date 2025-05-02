// https://leetcode.com/problems/repeated-substring-pattern/

package main

import "fmt"

func repeatedSubstringPattern(s string) bool {
	n := len(s)
	fmt.Println(n)
	for step := 1; step <= n/2; step++ {
		if n%step != 0 {
			continue
		}

		pattern := s[:step]
		isMatched := true
		fmt.Println(pattern, step)
		for i := step; i < n; i += step {
			if s[i:i+step] != pattern {
				isMatched = false
				break
			}
		}

		if isMatched {
			return true
		}
	}

	return false
}

func main() {
	s := "abcabcaabc"

	fmt.Println(repeatedSubstringPattern(s))
}
