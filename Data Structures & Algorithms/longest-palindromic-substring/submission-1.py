class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res_ind = 0
        res_len = 0

        n = len(s)
        for i in range(n):
            
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_ind = l
                    res_len = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_ind = l
                    res_len = r - l + 1
                l -= 1
                r += 1
        
        return s[res_ind : res_ind + res_len]