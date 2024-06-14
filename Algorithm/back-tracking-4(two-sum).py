def solution(nums, target):
    def back_tracking(start, curr):
        if len(curr) == 3 and sum(nums[i] for i in curr) == target:
            return curr
        
        for i in range(start, len(nums)):
            curr.append(i)
            res = back_tracking(i + 1, curr)
            if res:
                return res
            curr.pop()
        return None
    return back_tracking(0, [])

print(solution(nums = [4, 9, 7, 5, 1], target = 15))