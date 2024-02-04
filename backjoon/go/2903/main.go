// https://www.acmicpc.net/problem/2903 [중앙 이동 알고리즘]
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

	var N int
	fmt.Fscan(reader, &N)

	arr := make([]int, N+1)
	arr[0] = 2
	arr[1] = 3 //9
	for i := 1; i<=N; i++ {
		arr[i] = arr[i-1] * 2 -1
	}

	fmt.Fprintf(writer, "%d\n", arr[N]*arr[N])
}