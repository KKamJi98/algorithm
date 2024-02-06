// https://www.acmicpc.net/problem/2745 [진법 변환]
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	n := map[rune]int{}
	var str string
	var b int

	fmt.Fscan(reader, &str, &b)

	for i := 0; i < b; i++ {
		if i < 10 {
			n[rune('0'+i)] = i
		} else {
			n[rune('A'+i-10)] = i
		}
	}

	var result int
	for idx, value := range str {
		result += n[value] * int(math.Pow(float64(b), float64(len(str)-1-idx)))
	}
	fmt.Fprintln(writer, result)
}
