class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        if amount == 0:
            return 0
        
        q = deque([0])