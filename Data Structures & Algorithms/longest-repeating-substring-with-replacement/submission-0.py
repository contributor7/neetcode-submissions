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
        count = {}
        res = 0

        left = 0
        max_freq = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1 # GFFCA and GFFC work
            res = max(res, right - left + 1)

        return res