class Solution:
    def climbStairs(self, n: int) -> int:
        # 1 or 2 steps at a time
        # n steps required

        ways_to_reach_current_step, ways_to_reach_previous_step = 1, 1

        for i in range(n - 1): # 5 - 1 would be 0,1,2,3 in range, so this is gonna run 4 times
            temp = ways_to_reach_current_step
            ways_to_reach_current_step += ways_to_reach_previous_step
            ways_to_reach_previous_step = temp
        
        return ways_to_reach_current_step