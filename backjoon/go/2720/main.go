// https://www.acmicpc.net/problem/2720 [세탁소 사장 동혁]
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var T int
	fmt.Fscan(reader, &T)

	for i := 0; i < T; i++ {
		var C int
		fmt.Fscan(reader, &C)
		getExchange(C, writer)
	}
}

func getExchange(C int, writer *bufio.Writer) {
	arr := []int{
		25, 10, 5, 1,
	}

	for C > 0 {
		if C == 0 {
			break
		}
		for _, coin := range arr {
			fmt.Fprintf(writer, "%d ", C/coin)
			C = C % coin
		}
	}
	fmt.Fprintln(writer, "")
}
