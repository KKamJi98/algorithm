// https://www.acmicpc.net/problem/25206 [너의 평점은]
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main(){
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var totalScore float64
	var totalDegree float64
	for i:=0; i<20; i++{
		var str []string
		var strIn string
		strIn, _ = reader.ReadString('\n')
		strIn = strings.TrimSpace(strIn)
		
		str = strings.Split(strIn, " ")
		// fmt.Println(len(str))

		if str[2] == "P" {
			continue
		}
		degree, _ := strconv.ParseFloat(str[1], 64)
		totalScore += degree * getPoint(str[2])
		totalDegree += degree
	}

	fmt.Fprintln(writer, totalScore / totalDegree)
}

func getPoint(point string) float64 {
	if point == "A+" {
		return 4.5
	} else if point == "A0"{
		return 4.0
	} else if point == "B+"{
		return 3.5
	} else if point == "B0"{
		return 3.0
	} else if point == "C+"{
		return 2.5
	} else if point == "C0"{
		return 2.0
	} else if point == "D+"{
		return 1.5
	} else if point == "D0"{
		return 1.0
	} else if point == "F"{
		return 0.0
	} else {
		fmt.Println("error occurred")
		return -1
	}
}