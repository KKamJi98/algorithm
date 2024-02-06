package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	friends := []string{"muzi", "ryan", "frodo", "neo"}
	gifts := []string{"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"}

	solution(friends, gifts)
}

func solution(friends []string, gifts []string) int {
	friendMap := make(map[string]int)

	for _, friend := range friends {
		friendMap[friend] = 0
	}

	for _, gift := range gifts {
		giftSlice := strings.Split(" ", gift)
		friendMap[giftSlice[0]]++
		friendMap[giftSlice[1]]--
	}

	for key, gift range friendMap {
		if gift ==  {
			
		}
	}
}