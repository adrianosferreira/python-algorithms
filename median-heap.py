from heapq import *


class Median:

    def __init__(self):
        self.median = None
        self.left = []
        self.right = []

    def add(self, v):

        if not self.median:
            heappush(self.left, v * -1)
            self.median = self.left[0] * -1
            return

        if v < self.median:
            heappush(self.left, v * -1)
        else:
            heappush(self.right, v)

        if len(self.left) - len(self.right) > 1:
            temp = heappop(self.left)
            heappush(self.right, temp * -1)
        elif len(self.right) - len(self.left) > 1:
            temp = heappop(self.right)
            heappush(self.left, temp * -1)

        if len(self.left) == len(self.right):
            self.median = (self.left[0] * -1 + (self.right[0]))/2
        elif len(self.left) > len(self.right):
            self.median = self.left[0] * -1
        else:
            self.median = self.right[0]

    def get(self):
        return self.median


median = Median()
median.add(1)
median.add(2)
median.add(3)
median.add(5)
print(median.get())