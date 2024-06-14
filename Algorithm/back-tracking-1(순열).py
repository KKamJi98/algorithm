# nums= [1, 2, 3, 4]로 만들 수 있는 모든 순열 반환

def permute(nums):
    def back_track(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        
        for num in nums:
            if num not in curr:
                curr.append(num)
                back_track(curr)
                curr.pop()
                
    ans = []
    back_track([])
    return ans

result = permute([1, 2, 3, 4])
for i in result:
    print(i)