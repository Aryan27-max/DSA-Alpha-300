# ============================================================
# Day 27 - VARIANT: Design Circular Deque  (LeetCode 641)
# ============================================================
# The question:
#   MyCircularDeque(k) - a double-ended queue holding at most k items:
#     insertFront(v), insertLast(v)  -> True / False if full
#     deleteFront(), deleteLast()    -> True / False if empty
#     getFront(), getRear()          -> item or -1
#     isEmpty(), isFull()
#
# The big idea (two-ended fixed ring):
#   Same ring as the circular queue (head + count), plus two moves:
#     insertFront: step head BACKWARDS: head = (head - 1 + k) % k
#     deleteLast:  just count -= 1 (the back slot is computed from head)
#   The "+ k" keeps the index from going negative before the % k.
#   Every op is O(1).
# ============================================================


class MyCircularDequeBrute:
    # Plain list; insert(0) and pop(0) shift everything -> O(n).
    def __init__(self, k):
        self.k = k
        self.items = []

    def insertFront(self, value):
        if len(self.items) == self.k:
            return False
        self.items.insert(0, value)
        return True

    def insertLast(self, value):
        if len(self.items) == self.k:
            return False
        self.items.append(value)
        return True

    def deleteFront(self):
        if not self.items:
            return False
        self.items.pop(0)
        return True

    def deleteLast(self):
        if not self.items:
            return False
        self.items.pop()
        return True

    def getFront(self):
        return self.items[0] if self.items else -1

    def getRear(self):
        return self.items[-1] if self.items else -1

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.k


class MyCircularDeque:
    def __init__(self, k):
        self.k = k
        self.buf = [0] * k
        self.head = 0
        self.count = 0

    def insertFront(self, value):
        if self.count == self.k:
            return False
        self.head = (self.head - 1 + self.k) % self.k     # step back (wrapping)
        self.buf[self.head] = value
        self.count += 1
        return True

    def insertLast(self, value):
        if self.count == self.k:
            return False
        self.buf[(self.head + self.count) % self.k] = value
        self.count += 1
        return True

    def deleteFront(self):
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.k
        self.count -= 1
        return True

    def deleteLast(self):
        if self.count == 0:
            return False
        self.count -= 1                                   # back slot simply stops counting
        return True

    def getFront(self):
        return -1 if self.count == 0 else self.buf[self.head]

    def getRear(self):
        return -1 if self.count == 0 else self.buf[(self.head + self.count - 1) % self.k]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.k


if __name__ == "__main__":
    d = MyCircularDeque(3)
    print(d.insertLast(1), d.insertLast(2), d.insertFront(3), d.insertFront(4))  # True True True False
    print(d.getRear())       # 2
    print(d.isFull())        # True
    print(d.deleteLast())    # True
    print(d.insertFront(4))  # True
    print(d.getFront())      # 4
