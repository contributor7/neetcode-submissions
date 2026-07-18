'''
UPI
U: given a string of uppercase characters, replace as many as k letters to find the longest substring of
    repeating characters

P: substring problem -> pattern match to 2 pointers or sliding window
    iterate through the string, get current letter, start count, and replace all next letters if they do not match
    up to k times. then start again from the next letter. still O(n) since we do not traverse the entire same data
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        res = 0
        count = {}

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res