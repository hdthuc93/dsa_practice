// https://leetcode.com/problems/merge-sorted-array/description/

package main

import (
	"fmt"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	i := m + n - 1
	m = m - 1
	n = n - 1
	for i >= 0 && m >= 0 && n >= 0 {
		if nums1[m] >= nums2[n] {
			nums1[i] = nums1[m]
			m -= 1
		} else {
			nums1[i] = nums2[n]
			n--
		}
		i--
	}

	for i >= 0 {
		if m >= 0 {
			nums1[i] = nums1[m]
			m--
		}
		if n >= 0 {
			nums1[i] = nums2[n]
			n--
		}
		i--
	}
}

func main() {
	// nums1 := []int{1, 2, 3, 0, 0, 0}
	// m := 3
	// nums2 := []int{2, 5, 6}
	// n := 3

	// nums1 := []int{1}
	// m := 1
	// nums2 := []int{}
	// n := 0

	nums1 := []int{0}
	m := 0
	nums2 := []int{1}
	n := 1

	merge(nums1, m, nums2, n)
	fmt.Print(nums1)
}
