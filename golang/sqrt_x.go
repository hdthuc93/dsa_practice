// https://leetcode.com/problems/sqrtx/

package main

import "fmt"

func mySqrt(x int) int {
	if x == 1 {
		return 1
	}

	l, r := 1, x
	for l < r {
		m := (l + r) / 2
		if m*m == x {
			return m
		} else if m*m > x {
			r = m
		} else {
			l = m + 1
		}
	}

	return l - 1
}

func main() {
	x := 2147483638

	fmt.Println(mySqrt(x))
}
