class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None

        left = 0
        right = len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] < nums[right]:
                right = middle # not -1 since itd skip when next to left
            else:
                left = middle + 1

        return nums[left]