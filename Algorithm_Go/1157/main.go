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

	var strIn string
	fmt.Fscanln(reader, &strIn)

	var alphaMap = map[byte]int{}

	// initialize
	for i := 'A'; i <= 'Z'; i++ {
		alphaMap[byte(i)] = 0
	}

	for i := 0; i < len(strIn); i++ {
		if 'a' <= strIn[i] && strIn[i] <= 'z' {
			alphaMap[byte(strIn[i])-('a'-'A')]++
		} else {
			alphaMap[byte(strIn[i])]++
		}

	}

	var maxString string
	var maxCount int = 0
	for key, value := range alphaMap {
		if value < maxCount {
			continue
		} else if value > maxCount {
			maxString = string(key)
			maxCount = value
		} else if value == maxCount {
			maxString = "?"
		}
	}

	fmt.Fprintln(writer, maxString)
}
