class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        l, r = 0, 0
        total = 0

        # start, end = 0, 0

        while r < len(nums):
            # print(nums[r], total)

            if nums[r] >= total and total + nums[r] < nums[r]:
                # start = r
                # print(nums[r])
                total = 0
            total += nums[r]
            r += 1
        return total