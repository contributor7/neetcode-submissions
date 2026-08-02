class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_total = 0
        max_subarray_sum = nums[0]

        for num in nums:
            # other sol but then does not allow us to return indices as easily in a follow-up
            current_total = max(num, num + current_total)
            max_subarray_sum = max(max_subarray_sum, current_total)

        return max_subarray_sum