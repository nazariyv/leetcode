package main

import "fmt"

func maxProfit(prices []int) int {
	var m, p int
	for i := 1; i < len(prices); i++ {
		p = prices[i] - prices[i-1]
		if p > 0 {
			m = m + p
		}
	}
	return m
}

func main() {
	p := maxProfit([]int{7, 1, 5, 3, 6, 4})
	fmt.Println(p)
}
