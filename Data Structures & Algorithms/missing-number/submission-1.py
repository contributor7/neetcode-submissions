class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums) 
        xorr = n
        for i, num in enumerate(nums):

            # res += i - num # since missingNumber is [0, n], we can
        # subtract i because 1 - 1 = 0 if num[i] not missing
            
            xorr ^= i ^ num
        return xorr