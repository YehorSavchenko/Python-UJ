from random import randint


class RandomQueue:

    def __init__(self):
        self.n = 0
        self.items = []

    def insert(self, item):
        self.items.append(item)
        self.n += 1

    def remove(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')
        rand_index = randint(0, self.n - 1)
        rand_item = self.items[rand_index]
        self.items[rand_index] = self.items[self.n - 1]
        self.n -= 1
        self.items.pop(self.n)
        return rand_item

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):
        for i in range(self.n):
            self.remove()


random_queue = RandomQueue()
random_queue.insert(4)
random_queue.insert(8)
random_queue.insert(6)
random_queue.insert(7)
random_queue.insert(8)
random_queue.insert(1)
random_queue.insert(2)
random_queue.insert(3)
print(random_queue.items)
random_queue.remove()
random_queue.remove()
random_queue.remove()
print(random_queue.items)
