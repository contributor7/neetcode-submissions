from collections import heapq
import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        # self.min_val = None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            this_min = min(val, self.stack[-1][1])
            self.stack.append((val, this_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
