class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # LIFO
        res = []
        stack = []
        # for temp in temperatures:
        n = len(temperatures)
        # brute force
        for i in range(n):
            days = -1
            for k in range(i, n):
                days += 1
                if temperatures[k] > temperatures[i]:
                    res.append(days)
                    break
                if k == n - 1:
                    res.append(0)

        return res