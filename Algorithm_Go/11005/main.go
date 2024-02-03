// https://www.acmicpc.net/problem/11005 [진법 변환2]
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

	var N, B int
	fmt.Fscan(reader, &N, &B)

	var result []string

	for {
		tmp := N % B
		if tmp < 10 {
			result = append(result, fmt.Sprintf("%d", tmp))
		} else {
			result = append(result, fmt.Sprintf("%c", 'A'+tmp-10))
		}

		N /= B

		if N == 0 {
			break
		}
	}

	for i := len(result) - 1; i >= 0; i-- {
		fmt.Fprintf(writer, "%s", result[i])
	}
}
