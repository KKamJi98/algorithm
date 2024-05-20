# https://leetcode.com/problems/valid-parentheses/description/

#! Intuition
# This problem was solved using the properties of the Stack data structure.

#! Approach
# To reduce the amount of code, when '(' appears, ')' is added to the stack, when '{' appears, '}' is added, and when '[' appears, ']' is added to the stack.

#! Time complexity:
# O(n) 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == '(':
                stack.append(')')
            elif p == '{':
                stack.append('}')
            elif p == '[':
                stack.append(']')
            else:
                if not stack or stack.pop() != p:
                    return False
        return not stack
    
S = Solution()
print(S.isValid('['))