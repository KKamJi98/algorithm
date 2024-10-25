from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_alpha_dict = defaultdict(int)
        t_alpha_dict = defaultdict(int)

        for char_s, char_t in zip(s, t):
            if char_s in s_alpha_dict:
                s_alpha_dict[char_s] += 1

            if char_t in t_alpha_dict:
                t_alpha_dict[char_t] += 1

        for char_s in s_alpha_dict:
            if (
                char_s not in t_alpha_dict
                or s_alpha_dict[char_s] != t_alpha_dict[char_s]
            ):
                return False
        return True


test_solution = Solution()
print(test_solution.isAnagram("a", "a"))
