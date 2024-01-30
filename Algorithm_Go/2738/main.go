// https://www.acmicpc.net/problem/2738 [행렬 덧셈]
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
	var M int

	fmt.Fscanln(reader, &N, &M)

	A := make([][]int, N)
	for i := range A {
		A[i] = make([]int, M)
	}

	B := make([][]int, N)
	for i := range B {
		B[i] = make([]int, M)
	}

	C := make([][]int, N)
	for i := range C {
		C[i] = make([]int, M)
	}

	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			fmt.Fscan(reader, &A[i][j])
		}
	}
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			fmt.Fscan(reader, &B[i][j])
		}
	}
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			C[i][j] = A[i][j] + B[i][j]
			fmt.Fprintf(writer, "%v ", C[i][j])
		}
		fmt.Fprintln(writer)
	}
}
