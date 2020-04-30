class Heap:

    def __init__(self):
        self.data = []

    def insert(self, v):
        self.data.append(v)

        curr = len(self.data) - 1
        while True:
            parent = self.get_parent_index(curr)

            if self.data[parent] > self.data[curr]:
                temp = self.data[parent]
                self.data[parent] = self.data[curr]
                self.data[curr] = temp
                curr = parent
            else:
                break

    def pop(self):
        if not self.data:
            return None

        res = self.data[0]
        self.data[0] = self.data.pop()
        curr = 0

        while True:
            if self.has_left_child(curr) and self.data[curr] > self.data[self.get_left_child(curr)]:
                temp = self.data[curr]
                self.data[curr] = self.data[self.get_left_child(curr)]
                self.data[self.get_left_child(curr)] = temp
                curr = self.get_left_child(curr)
            elif self.has_right_child(curr) < len(self.data) and self.data[curr] > self.data[self.get_right_child(curr)]:
                temp = self.data[curr]
                self.data[curr] = self.data[self.get_right_child(curr)]
                self.data[self.get_right_child(curr)] = temp
                curr = self.get_right_child(curr)
            else:
                break

        return res

    def peek(self):
        if not self.data:
            return None

        return self.data[0]

    def get_left_child(self, parent):
        return int((parent * 2) + 1)

    def get_right_child(self, parent):
        return int((parent * 2) + 2)

    def get_parent_index(self, child):
        return int((child - 1) / 2)

    def heapify(self, data):
        for x in data:
            self.insert(x)

    def has_left_child(self, parent):
        return self.get_left_child(parent) < len(self.data)

    def has_right_child(self, parent):
        return self.get_right_child(parent) < len(self.data)


heap = Heap()
heap.heapify([5, 1, 3, 10, 11, 15, 8])
print(heap.data)
