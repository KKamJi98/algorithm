// https://www.acmicpc.net/problem/2444 별찍기
package main

import (
	"fmt"
)

func main() {
	var num int
	fmt.Scanln(&num)

	for i := 1; i < num; i++ {
		for k := num - i; k >= 1; k-- {
			fmt.Printf(" ")
		}
		for j := 1; j <= i*2-1; j++ {
			fmt.Printf("*")
		}
		fmt.Println()
	}

	for i := 1; i <= num*2-1; i++ {
		fmt.Printf("*")
	}
	fmt.Println()

	for i := num - 1; i >= 1; i-- {
		for k := num - i; k >= 1; k-- {
			fmt.Printf(" ")
		}
		for j := 1; j <= i*2-1; j++ {
			fmt.Printf("*")
		}
		if i == 1 {
			continue
		}
		fmt.Println()
	}
}
