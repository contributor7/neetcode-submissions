class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums) # don't need the .copy() function here 
        # since set is a different type of object than a list
        if len(my_set) < len(nums):
            return True
        else:
            return False
        # or simply
        # return len(set(nums)) < len(nums)