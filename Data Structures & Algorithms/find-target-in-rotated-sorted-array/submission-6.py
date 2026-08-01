class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else: # since it was sorted and we checked if the
            # left side was in ascending and it wasn't, the right half is, 
            # so nums[r] >= nums[m]
                if nums[m] <= target or nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
                # if nums[m] > target or nums[r] < target:
                #     r = m - 1
                # else:
                #     l = m + 1
        return - 1