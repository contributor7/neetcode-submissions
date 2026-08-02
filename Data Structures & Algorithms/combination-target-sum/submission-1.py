'''
start from 

'''


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort() # here we sort it

        def dfs(i, cur, total): # dfs since we search the current number repeatedly and hten all next numbers with it, before removing a frequency and checking again
            if total == target:
                res.append(cur.copy()) # copy() since int list is mutable, unlike str list
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        # O(2 ^ (target/min)) time complexity since I can go up to target/min deep, and this is the height
        # since at every number I have 2 options, either add it or skip it

        # space complexity is O(target/min), but includinig the output res would be O(solutions * target/min)
        # since like if target/min = 8/2, then i have an arr of len 4, adn this is 1 valid solution
        dfs(0, [], 0)
        return res