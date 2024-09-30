# https://school.programmers.co.kr/learn/courses/30/lessons/250137 - [붕대 감기]


def solution(bandage, health, attacks):
    maxHealth = health
    lastAttackTime = attacks[len(attacks) - 1][0]

    attackCount = 0
    continuedRecovery = 0
    for i in range(0, lastAttackTime + 1):
        # 공격을 당했을 경우
        if i == attacks[attackCount][0]:
            continuedRecovery = 0
            health -= attacks[attackCount][1]
            attackCount += 1
            if health <= 0:
                return -1
            print(f"{i} => {health}")
            continue
        else:  # 공격을 당하지 않았을 경우
            continuedRecovery += 1
            if continuedRecovery == bandage[0]:
                health += bandage[2] + bandage[1]
                continuedRecovery = 0
            else:
                health += bandage[1]

            if health > maxHealth:
                health = maxHealth
            print(f"{i} => {health}")
    return health


if __name__ == "__main__":
    # [시전 시간, 초당 회복량, 추가 회복량]
    bandageIn = [4, 2, 7]
    maxHealthIn = 20
    attacks = [[1, 15], [5, 16], [8, 6]]
    print(solution(bandageIn, maxHealthIn, attacks))
