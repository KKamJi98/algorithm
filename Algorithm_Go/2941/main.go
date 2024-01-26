// https://www.acmicpc.net/problem/2941 [크로아티아 알파벳]
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	croatia := []string{"c=", "c-", "z=", "dz=", "d-", "lj", "nj", "s="}

	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var strIn string
	fmt.Fscanln(reader, &strIn)

	var count int = len(strIn)
	for idx := 0; idx <= len(strIn)-2; idx++ {
		if idx <= len(strIn)-3 && strIn[idx:] == "dz=" {
			count -= 2
			idx += 2
			break
		}
		for _, croatiaAlpha := range croatia {
			if len(croatiaAlpha) == 3 && idx == len(strIn)-2 {
				continue
			}
			if strIn[idx:idx+len(croatiaAlpha)] == croatiaAlpha {
				if croatiaAlpha == "dz=" {
					count -= 2
				} else {
					count--
				}
				idx += len(croatiaAlpha) - 1
				break
			}
		}
	}

	fmt.Fprintln(writer, count)
}
