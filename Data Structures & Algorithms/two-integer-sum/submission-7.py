class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_indices = []
        size = len(nums)
        # for i in range(size): # [0, 1 , 2, 3]
        #     for j in range(i + 1, size):
        #         if nums[i] + nums[j] == target:
        #             ans_indices += i, j

        diff = {}
        # for i in range(size):
        #     diff.update({target - nums[i]: i})

        # for j in range(size): # starts at 0
        #     if nums[j] in diff and j < diff[nums[j]]:
        #         # ans_indices.append([j, diff[nums[j]]])
        #         return [j, diff[nums[j]]]

        for i, num in enumerate(nums):
            if num in diff:
                return [diff[nums[i]], i]   # 7 - 4 = 3
            diff[target - num] = i
            print(diff)


        # return ans_indices