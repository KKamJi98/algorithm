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
	friendMapScore := make(map[string]int)
	friendMapTo := make(map[string][string]int)

	for _, friend := range friends {
		friendMap[friend] = 0
		for _, To := range friends {
			friendMapTo[friend][To] = 0
		}
	}

	for _, gift := range gifts {
		giftSlice := strings.Split(" ", gift)
		friendMapTo[giftSlice[0][giftSlice[1]]]++
		friendMap[giftSlice[0]]++
		friendMap[giftSlice[1]]--
	}

	for from, to := range friendMapTo {
		for _, count := range to {
			if friendMapTo[from][to] == friend[to][from] {
				if friendMapScore[from] < friendMapScore[to] {
					friendMapScore[to]++
				} else if friendMapScore[from] > friendMapScore[to] {
					friendMapScore[from]++
				} else {
					continue
				}
			} else {
				if friendMapTo[from][to] < friendMapTo[to][from] {
					friendMapScore[from]++
				} else if friendMapTo[from][to] > friendMapTo[to][from] {
					friendMapScore[to]++
				} else {
					continue
				}
			}
		}
	}

	for key, gift range friendMap {
		if gift ==  {
			
		}
	}
}