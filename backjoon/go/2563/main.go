// https://www.acmicpc.net/problem/2563 색종이

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

	matrix := make([][]bool, 100)
	for i := range matrix {
		matrix[i] = make([]bool, 100)
	}

	var num int
	fmt.Fscan(reader, &num)

	var paper [][]int
	paper = make([][]int, num)
	for i := range paper {
		paper[i] = make([]int, 2)
		fmt.Fscan(reader, &paper[i][0], &paper[i][1])
	}

	for i := 0; i < num; i++ {
		//사진의 좌표부터 시작
		for x := paper[i][0]; x < paper[i][0]+10; x++ {
			for y := paper[i][1]; y < paper[i][1]+10; y++ {
				matrix[x][y] = true
			}
		}
	}

	area := 0

	for _, i := range matrix {
		for _, j := range i {
			if j {
				area++
			}
		}
	}

	fmt.Fprintf(writer, "%v", area)
}
