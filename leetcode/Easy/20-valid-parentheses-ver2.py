# https://leetcode.com/problems/valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}
        open_brackets = set(bracket_map.values())

        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                return False

        return not stack


solution_test = Solution()
print(solution_test.isValid("(])"))  # 출력: False
print(solution_test.isValid("()[]{}"))  # 출력: True
print(solution_test.isValid("([)]"))  # 출력: False
print(solution_test.isValid("{[]}"))  # 출력: True
