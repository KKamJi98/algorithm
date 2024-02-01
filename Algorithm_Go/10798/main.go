// https://www.acmicpc.net/problem/10798 [세로읽기]
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	// "strconv"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	stringArray := make([][]rune, 5)
	for i := 0; i < 5; i++ {
		stringArray[i] = make([]rune, 15)
		var line string
		line, _ = reader.ReadString('\n')
		line = strings.TrimSpace(line)
		stringArray[i] = []rune(line)
	}

	for i := 0; i < 15; i++ {
		for j := 0; j < 5; j++ {
			if i < len(stringArray[j]) {
				fmt.Fprintf(writer, string(stringArray[j][i]))
			}
		}

	}
}
