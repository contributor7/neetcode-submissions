class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_total = 0
        max_subarray_sum = nums[0]

        for num in nums:
            if current_total < 0:
                current_total = 0

            current_total += num
            max_subarray_sum = max(max_subarray_sum, current_total)

        return max_subarray_sum