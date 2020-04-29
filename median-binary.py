class Median:

    def __init__(self):
        self.data = []

    def add(self, v):
        if not self.data:
            self.data.append(v)
            return

        left = 0
        right = len(self.data) - 1

        while left <= right:
            mid = left + int(((right - left)/2))

            if v < self.data[mid]:
                right = mid - 1
            else:
                left = mid + 1

        self.data.insert(left, v)

    def get(self):
        if not self.data:
            return 0

        mid = len(self.data)/2
        if len(self.data) % 2 > 0:
            return self.data[int(mid)]
        else:
            return (self.data[int(mid)] + self.data[int(mid)-1])/2


median = Median()
median.add(1)
median.add(2)
median.add(3)
median.add(5)
print(median.get())
