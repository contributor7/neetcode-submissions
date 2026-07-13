class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set(nums)
        if len(uniques) < len(nums):
            return True
        return False

        # return len(set(nums)) < len(nums)