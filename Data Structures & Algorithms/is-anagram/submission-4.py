class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # s.sort()
        # t.sort() only works for lists not arrays

        # if sorted(s) != sorted(t):
        #     return False
        # return True
        # above is O(n log n) due to sorted(), need O(n + m)
        # anagram means the same characters, diff order
        
        arr = []

        for c in t:
            arr.append(c)

        for c in s:
            if c not in arr or s.count(c) != t.count(c):
                return False
        return True