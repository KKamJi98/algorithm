# nums = [1,2,3,4]로 만들 수 있는 부분집합을 모두 반환하시오


def solution(nums):
    result = []

    def back_tracking(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return

        for i in range(start, len(nums)):
            curr.append(nums[i])
            back_tracking(i + 1, curr)
            curr.pop()

    for k in range(len(nums) + 1):
        back_tracking(start=0, curr=[])
    return result


print(solution(nums=[1, 2, 3, 4]))
