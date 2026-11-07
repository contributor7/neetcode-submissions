class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)
        # if n < 2:
        #     return [0]
        # # LIFO
        # res = []
        # stack = []
        # # for temp in temperatures:
        # max_temp = 0

        # for i in range(n):
        #     curr = temperatures.pop()
        #     if curr > max_temp:
        #         days = i + 1
        #         max_temp = curr

        #     if curr < max_temp:
        #         res.append(days)
        #         max_temp = curr
        #     else:
        #         res.append(0)
        # res.reverse()

        res = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res