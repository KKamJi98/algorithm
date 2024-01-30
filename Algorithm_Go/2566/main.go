// https://www.acmicpc.net/problem/2566 [최댓값]
package main

import (
	"fmt"
	"bufio"
	"os"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var maxRow, maxCol, maxValue int
	
	numMatrix := make([][]int, 9)
	for i := range numMatrix {
		numMatrix[i] = make([]int, 9)
	}

	for i := range numMatrix {
		for j := range numMatrix {
			fmt.Fscan(reader, &numMatrix[i][j])
			if numMatrix[i][j] > maxValue {
				maxValue = numMatrix[i][j]
				maxRow = i
				maxCol = j
			}
		}
	}

	fmt.Fprintf(writer, "%v\n%v %v", maxValue, maxRow+1, maxCol+1)
}