from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.data.popleft()

    def search(self, index):
        if index < 0:
            raise IndexError
        return self.data[index]

    def is_empty(self):
        return not bool(len(self.data))
