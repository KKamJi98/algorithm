// https://www.acmicpc.net/problem/1157 단어공부
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var alphaCount [26]int
	var strIn string
	fmt.Fscanln(reader, &strIn)

	for _, alpha := range strIn {
		if 'a' <= alpha && alpha <= 'z' {
			alphaCount[alpha-'a']++
		} else if 'A' <= alpha && alpha <= 'Z' {
			alphaCount[alpha-'A']++
		}
	}

	var maxString string
	var maxCount int
	for idx, count := range alphaCount {
		if count > maxCount {
			maxString = string('A' + idx)
			maxCount = count
		} else if count == maxCount {
			maxString = "?"
		}
	}

	fmt.Fprintln(writer, maxString)
}
