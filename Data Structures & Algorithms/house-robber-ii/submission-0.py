class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0
        n = len(nums)
        for i in range(n - 1):
            num = nums[i]

            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        rob_start = rob2

        rob1, rob2 = 0, 0
        for i in range(1, n):
            num = nums[i]

            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        rob_end = rob2
        return max(rob_start, rob_end)