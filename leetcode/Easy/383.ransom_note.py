# https://leetcode.com/problems/ransom-note/

from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = defaultdict(int)

        for char_ele in magazine:
            magazine_dict[char_ele] += 1

        for char_ele in ransomNote:
            if magazine_dict[char_ele] == 0:
                return False
            magazine_dict[char_ele] -= 1
        return True


_solution = Solution()
print(_solution.canConstruct(ransomNote="aa", magazine="ab"))
