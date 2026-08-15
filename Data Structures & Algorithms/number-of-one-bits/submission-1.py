class Solution:
    def hammingWeight(self, n: int) -> int:
        num = 0
        while n: # max iteration of 32 times
            num += n & 1
            n = n >> 1
            # n >> 1 # does not work alone
        return num
