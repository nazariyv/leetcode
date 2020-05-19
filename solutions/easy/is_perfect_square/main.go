package main

import (
	"fmt"
	"math"
)

func fx(x float64, num float64) float64 {
	return math.Pow(x, 2) - num
}

func fxPrime(x float64) float64 {
	return 2.0 * x
}

func isPerfectSquare(num int) bool {
	x := float64(num / 2)
	numFloat := float64(num)
	fmt.Println(numFloat)
	epsilon := 0.000001
	var sqr float64

	for {
		sqr = fx(x, numFloat)
		if sqr > epsilon {
			x = x - sqr/fxPrime(x)
		} else {
			break
		}
	}

	fmt.Println(math.Mod(x, 1))
	isWhole := math.Mod(x, 1) < epsilon
	fmt.Println((x))
	return isWhole && (math.Pow(x, 2)-numFloat) < epsilon
}

func main() {
	fmt.Println(isPerfectSquare(5))
}
