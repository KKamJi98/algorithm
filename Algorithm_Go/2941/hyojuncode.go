package main

import (
	"bufio"
	"fmt"
	"os"
)

func hyujun() {
	croatia := []string{"c=", "c-", "dz", "d-", "lj", "nj", "s=", "z="}

	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var stringIn string
	append(stringIn, "*")
	fmt.Fscanln(reader, &stringIn)
	count := 0
	for idx := 0; idx < len(stringIn); idx++ {
		if idx == len(stringIn)-1 {
			count++
			break
		}
		for i := 0; i < len(croatia); i++ {
			if stringIn[idx:idx+2] == croatia[i] {
				if i == 2 {
					if stringIn[idx+2] == '=' {
						idx += 2
					}
				} else {
					idx++
				}
				break
			}
		}
		count++
	}

	fmt.Fprintln(writer, count)

	// for char := range stringIn {
	// 	myMap[]
	// }
}
