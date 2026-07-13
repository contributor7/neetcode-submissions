
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # cannot sort since that would not be O(n)


        # i could just do a sliding window

        if not prices:
            return 0
        lowest_price = prices[0]
        current_max = 0
        size = len(prices)

        for i in range(size):
            if prices[i] < lowest_price:   # 10 - 9999
                lowest_price = prices[i]
            
            current_max = max(prices[i] - lowest_price, current_max)
        return current_max