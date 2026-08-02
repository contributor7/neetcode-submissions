class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.small, -num)

        heapq.heappush(self.large, -heapq.heappop(self.small))
        # this also works but notice I changed to comparing whenever len_large > len_small, not + 1 anymore
        if len(self.large) > len(self.small):
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        small_len = len(self.small)
        large_len = len(self.large)
        
        if small_len > large_len:
            return -1 * self.small[0]
        if large_len > small_len:
            return self.large[0] # peek and not pop since I the program may call median several times on the same or a growing list, and is also faster than popping
        # if even
        return ( self.large[0] + -1 * self.small[0] ) / 2