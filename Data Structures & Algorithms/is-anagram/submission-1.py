class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # s.sort()
        # t.sort()
        if sorted(s) != sorted(t):
            return False
        return True