'''
UPI
U: given a string of uppercase characters, replace as many as k letters to find the longest substring of
    repeating characters

P: substring problem -> pattern match to 2 pointers or sliding window
    
    create a hashmap to store letter frequency
    track max freq
    iterate through the string with a right index
    increase letter frequency of right index,
    this is the start of a window, which should shrink if
    the (window size - maxf) > how many we can replace (k)
    we compare with maxf since we only want to replace in favor
    of the most frequent letters, to avoid checking all possible
    string variations since that the original most frequent letters
    would prove to be the longest anyway
    shrink the window size by incrementing left, and since that letter
    is out of the picture, decrease its hashmap frequency count
    update result with max(length of the current window, result)
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
# ABBCD, k = 1. when at C, correct window, then at D it is incorrect
# but the value of res (or the window size) is still the same.
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res