// lv1-가장많이받은선물
package main

import (
	"fmt"
	"strings"
)

func solution(friends []string, gifts []string) int {
	friendMapScore := make(map[string]int)
	friendMapTo := make(map[string]map[string]int)
	getCount := make(map[string]int)

	for _, friend := range friends {
		friendMapScore[friend] = 0
		friendMapTo[friend] = make(map[string]int)
		getCount[friend] = 0
	}

	for _, gift := range gifts {
		giftSlice := strings.Split(gift, " ")
		from, to := giftSlice[0], giftSlice[1]
		friendMapTo[from][to]++
		friendMapScore[from]++
		friendMapScore[to]--
	}

	
	for from, friendsMap := range friendMapTo {
		for to, _ := range friendsMap {
			//두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면,
			//선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
			if friendMapTo[from][to] == friendMapTo[to][from] {
				if friendMapScore[from] > friendMapScore[to] {
					getCount[from]++
				}
				} else { //두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
					if friendMapTo[from][to] > friendMapTo[to][from] {
							getCount[from]++
						} 
					}
				}
			}
			
			var maxCount int = 0
			for key, count := range getCount {
				fmt.Printf("%s : %d\n", key, count)
				if count > maxCount {
					maxCount = count
				}
			}

	return maxCount
}

func main() {
	friends := []string{"muzi", "ryan", "frodo", "neo"}
    gifts := []string{"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"}
    fmt.Println(solution(friends, gifts))
}