class MedianFinder:

    def __init__(self):
        # self.num = num
        pass
    
    nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        m = n // 2
        # [1, 2, 3, 4] len = 4, 4 // 2 = 2. even so do below

        if n % 2 == 0:
            return ( self.nums[m] + self.nums[m - 1] ) / 2
        else: # [1, 2, 3, 4, 5] len = 5,  5 // 2 = 2 which is odd, so return 
            return self.nums[m]