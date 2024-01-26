// https://www.acmicpc.net/problem/10988 펠린드롬인지 확인하기
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var strIn string

	fmt.Scanln(&strIn)

	strLen := len(strIn)
	// fmt.Printf("%T\t %v", strLen/2, strLen/2)
	var strCheck bool
	for i := 0; i < strLen; i++ {
		if strIn[strLen-i-1] != strIn[i] {
			strCheck = true
			break
		}
	}

	if strCheck == true {
		fmt.Println(0)
	} else {
		fmt.Println(1)
	}
}
