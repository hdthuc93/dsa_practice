// https://leetcode.com/problems/search-insert-position/

package main

import "fmt"

func searchInsert(nums []int, target int) int {
	l, r := 0, len(nums)

	for l < r {
		m := (l + r) / 2

		if nums[m] == target {
			return m
		} else if nums[m] > target {
			r = m
		} else {
			l = m + 1
		}
	}

	return l
}

func main() {
	var nums []int = []int{1, 3, 5, 7, 9}
	target := 8

	fmt.Println(searchInsert(nums, target))
}
