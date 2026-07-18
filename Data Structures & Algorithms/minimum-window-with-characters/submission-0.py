'''
UPI:

Understand:
Input: 2 strings: s and t
Output: string. shortest substring of s
Edge cases: len(t) > len(s), empty s or t

Plan:
Loop through s, if the current char == first char of t:
start the window. continue until end of s.
Problems with this approach:
returns longest substring

Solution:
need to 


Other approach:
can make a hashmap of each char in s and their index

then iterate through each char in t,
find the lowest 


need to check if any of the t chars are the current start char,
not just the first t char


so i need a hashmap of t chars (t_freq) so i can quickly compare if
s's char is in t map and the frequency, since i need to include dups
and a set would erase dup counting. Use collection's Counter

iterate through s via a for loop
if current s char in t_freq, reduce t_freq[s] by 1
(but then we will need to reset the count for new windows)
and start the window
append the current s char every iteration after the window is started
this gets us the longest substring
to get the shortest via comparing other paths, would need to brute force
each char's path with a default t_freq map each time. O(N^2) time complexity
sol: so what we would do is remove the left char if the next/right char
still makes the freq valid

reducing t_freq[s] by 1 when current s char in t_freq does not help
since s can have more duplicates and be fine and this would force us to
check when < 0 or when t_freq is satisfied

instead, let's make a hashmap for s as well, and increase (and
decrease when ajdusting window) that one as we go


instead, let's make a hashmap for current window, this allows us to
increase and decrease as needed, instead of s's pre-populated
'''
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: # if not s is handled by for loop (skipped)
            return ''
        # if len(t) > len(s): # handled by algo, through count. 
        #     # should be handled in algo anyway
        #     return ''

        t_freq = Counter(t)
        window = {}

        l = 0

        have = 0
        need = len(t_freq)

        res = [-1, -1]
        res_len = float('inf')

        for r, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in t_freq and window[char] == t_freq[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1 # decrease count before we move to next left index
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1
                
                l += 1
                # this process fast forwards to the rightmost required left
                # to make the window valid
        l, r = res # unpacks res into l and r

        return s[l : r + 1] if res_len != float('inf') else ''
        # r + 1 since splicing ends exclusive. [l,r) so need
        # [l, r + 1) to get [l,r] in splicing