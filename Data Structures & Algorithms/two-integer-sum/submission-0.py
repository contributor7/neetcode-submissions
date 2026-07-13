class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_indices = []
        size = len(nums)
        for i in range(size):
            for j in range(i, size):
                if i != j and nums[i] + nums[j] == target:
                    ans_indices += i, j

        # diff = []
        # for i in range(size):
        #     # diff += target - nums[i]
        #     diff.append(target - nums[i])

        # for j in range(size):
        #     if nums[j] == diff[j]:
        #         ans_indices.append(j)

        return ans_indices