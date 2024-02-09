// https://www.acmicpc.net/problem/24265 [ 알고리즘 수업 - 알고리즘의 수행 시간 4 ]

package main

import (
    "fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	var count int64

	for i := 1; i <= n-1; i++ {
		count += int64(i)
	}
	fmt.Println(count)
	fmt.Println(2)
}