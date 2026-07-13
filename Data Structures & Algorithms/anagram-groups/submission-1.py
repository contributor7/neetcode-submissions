from collections import defaultdict
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26 # 26 lowercase letters in alphabet, Each index represents a letter.
            for c in s:
                print(ord('a')) # = 97, to not be out of bounds
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())