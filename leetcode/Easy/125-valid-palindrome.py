class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_str = "".join(c.lower() for c in s if c.isalnum())

        for idx in range(0, len(only_str) // 2):
            if only_str[idx] != only_str[-(idx + 1)]:
                return False

        return True


test_solution = Solution()
print(test_solution.isPalindrome("A man, a plan, a canal: Panama"))
print(test_solution.isPalindrome("race a car"))
print(test_solution.isPalindrome(" "))
