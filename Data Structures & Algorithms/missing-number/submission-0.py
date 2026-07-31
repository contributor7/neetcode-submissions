class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # binary_numnary = 0
        res = len(nums) # since missingNumber is [0, n], we can later
        # subtract the index itself because 1 - 1 = 0 if num[i] not missing

        for i, num in enumerate(nums):
            # if num != binary_num:
            #     return binary_num_to_int
            # binary_num >> 1
            res += i - num
        return res