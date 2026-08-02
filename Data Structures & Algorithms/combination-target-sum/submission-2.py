'''
start from 

'''


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()

        def dfs(i, cur, total): # dfs since we search the current number and hten all next numbers with it, before removing a frequency and checking again
            if total == target:
                res.append(cur.copy()) # copy() since int list is mutable, unlike str list
                return

            if i >= len(nums) or total > target:
                return
            if total + nums[i] > target: # can add this if sorting beforehand
                return
            cur.append(nums[i])
            dfs(i, cur, total + nums[i]) # same as total += nums[i]. then after all the dfs(i + 1, ...,...) calls below occur, return here
            cur.pop()  # after we returned, pop the number that made total >= target to make space
            dfs(i + 1, cur, total) # do the same loop for the next index, with the current total < target

        # O(2 ^ (target/min)) time complexity since I can go up to target/min deep, and this is the height
        # since at every number I have 2 options, either add it or skip it

        # space complexity is O(target/min), but includinig the output res would be O(solutions * target/min)
        # since like if target/min = 8/2, then i have an arr of len 4, adn this is 1 valid solution
        dfs(0, [], 0)
        return res