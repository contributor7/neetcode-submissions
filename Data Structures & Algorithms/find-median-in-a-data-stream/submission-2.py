class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]: # if self.large is same as if len(self.large) != 0, empty arrs are falsey in Python
            heapq.heappush(self.large, num)
        else:
            val = -1 * num
            heapq.heappush(self.small, val)
        '''
        5, 4, 3, 2, 1, 7, 8

        small: -2, -1, -3, -4
        1, 2, 3, 4, 5, 7, 8

        large: 5, 7, 8
        '''
        small_len = len(self.small)
        large_len = len(self.large)
        if small_len > large_len + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val) # give large the largest number in small, by popping the smallest number after it became negative
        elif large_len > small_len + 1:
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