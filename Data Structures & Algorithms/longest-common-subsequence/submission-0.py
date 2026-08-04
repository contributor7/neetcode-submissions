
from collections import Counter


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        t1_map = Counter(text1)
        t2_map = Counter(text2)

        lowest_ind = 0
        res = 0

        for i, let in enumerate(text1):
            if let in t2_map:
                lowest_ind = min(lowest_ind, i)
                if t2_map[let] >= lowest_ind:
                    res += 1

        res1 = res
        res = 0
        lowest_ind = 0
        for i, let in enumerate(text2):
            if let in t1_map:
                lowest_ind = min(lowest_ind, i)
                if t1_map[let] < lowest_ind:
                    res += 1
        res2 = res
        return max(res1, res2)