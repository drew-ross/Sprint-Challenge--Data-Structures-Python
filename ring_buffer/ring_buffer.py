class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.write_head = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.write_head] = item
            self.write_head += 1
            if self.write_head >= len(self.storage):
                self.write_head = 0

    def get(self):
        return self.storage