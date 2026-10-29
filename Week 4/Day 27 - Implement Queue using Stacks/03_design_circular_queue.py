# ============================================================
# Day 27 - VARIANT: Design Circular Queue  (LeetCode 622)
# ============================================================
# The question:
#   MyCircularQueue(k) - a queue that holds at most k items:
#     enQueue(value) -> True if added, False if full
#     deQueue()      -> True if removed, False if empty
#     Front(), Rear() -> the front / back item, or -1 if empty
#     isEmpty(), isFull()
#
# The big idea (fixed-size ring):
#   One list of k slots that never grows. Track:
#     head  = index of the front item
#     count = how many items are stored
#   The back slot is (head + count - 1) % k, and the next free slot is
#   (head + count) % k. The % k makes the indexes wrap around to 0,
#   so freed slots at the start get reused. Every op is O(1).
# ============================================================


class MyCircularQueueBrute:
    # Plain list; deQueue uses pop(0), which shifts every element -> O(n).
    def __init__(self, k):
        self.k = k
        self.items = []

    def enQueue(self, value):
        if len(self.items) == self.k:
            return False
        self.items.append(value)
        return True

    def deQueue(self):
        if len(self.items) == 0:
            return False
        self.items.pop(0)
        return True

    def Front(self):
        return self.items[0] if self.items else -1

    def Rear(self):
        return self.items[-1] if self.items else -1

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.k


class MyCircularQueue:
    def __init__(self, k):
        self.k = k
        self.buf = [0] * k
        self.head = 0
        self.count = 0

    def enQueue(self, value):
        if self.count == self.k:
            return False
        self.buf[(self.head + self.count) % self.k] = value   # next free slot
        self.count += 1
        return True

    def deQueue(self):
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.k                  # front moves forward
        self.count -= 1
        return True

    def Front(self):
        return -1 if self.count == 0 else self.buf[self.head]

    def Rear(self):
        return -1 if self.count == 0 else self.buf[(self.head + self.count - 1) % self.k]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.k


if __name__ == "__main__":
    q = MyCircularQueue(3)
    print(q.enQueue(1), q.enQueue(2), q.enQueue(3), q.enQueue(4))   # True True True False
    print(q.Rear())       # 3
    print(q.isFull())     # True
    print(q.deQueue())    # True
    print(q.enQueue(4))   # True (reuses the freed slot)
    print(q.Rear())       # 4
    print(q.Front())      # 2
