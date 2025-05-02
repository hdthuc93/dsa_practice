// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

package main

import (
	"fmt"
)

func strStr(haystack string, needle string) int {
	i := 0
	for i < len(haystack) && len(haystack)-i >= len(needle) {
		j := 0
		ii := i
		for j < len(needle) && haystack[ii] == needle[j] {
			j++
			ii++
		}

		if j == len(needle) {
			return i
		}
		i += 1
	}

	return -1
}

func strStrImproved(haystack string, needle string) int {
	nNeedle := len(needle)
	for pos := range haystack {
		end := pos + nNeedle
		if end > len(haystack) {
			break
		}

		fmt.Printf("Type of %T\n", haystack[pos:end])
		if haystack[pos:end] == needle {
			return pos
		}
	}

	return -1
}

func main() {
	haystack := "aaaabbc"
	needle := "aaabbc"

	fmt.Println(strStr(haystack, needle))
	fmt.Println(strStrImproved(haystack, needle))
}
