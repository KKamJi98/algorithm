// https://www.acmicpc.net/problem/1316 [그룹 단어 체커]
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

	var N int
	fmt.Fscanln(reader, &N)
	var count int

	for i := 0; i < N; i++ {
		var strIn string
		fmt.Fscanln(reader, &strIn)

		var kkamSlice []rune
		var flag bool

		for idx, value := range strIn {
			if idx != 0 && strIn[idx] == strIn[idx-1] {
				continue
			} else {
				for _, value2 := range kkamSlice {
					if idx == 0 {
						break
					}
					if value == rune(value2) {
						flag = true
						break
					}
				}
				if flag == true {
					break
				}
			}
			kkamSlice = append(kkamSlice, value)
		}
		if flag == false {
			count++
		}
	}

	fmt.Fprintln(writer, count)
}
