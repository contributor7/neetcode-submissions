class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]

        prefix = suffix = 1

        for i in range(n):
            prefix = nums[i] * prefix
            suffix = nums[n - 1 - i] * suffix
            res = max(res, max(prefix, suffix))

        return res