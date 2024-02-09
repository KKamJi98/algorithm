// https://www.acmicpc.net/problem/24264 - [ 알고리즘 수업 -알고리즘의 수행 시간 3 ]
package main

import (
    "fmt"
	"math"
)

func main() {
	var n int64
	fmt.Scan(&n)

    fmt.Println(int64(math.Pow(float64(n), 2)));
	fmt.Println(2)
}