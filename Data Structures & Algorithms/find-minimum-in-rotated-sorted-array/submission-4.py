class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None

        minimum = nums[0]

        left = 0
        right = len(nums) - 1
        while left <= right: # to check when the min is the right or left value do <=
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])
                # print('break')
                break
            middle = (right + left) // 2
            minimum = min(minimum, nums[middle])
            if nums[middle] >= nums[left]: # does not move if same value without =
                left = middle + 1 # does not move in a 2-length window without =
            else:
                right = middle - 1

        return minimum