# ============================================================
# Day 25 - VARIANT: Design a Stack With Increment Operation  (LeetCode 1381)
# ============================================================
# The question:
#   CustomStack(maxSize):
#     push(x)          add x on top, unless the stack is full
#     pop()            remove and return the top, or -1 if empty
#     increment(k, v)  add v to the BOTTOM k elements (all of them if fewer than k)
#
#   Example: CustomStack(3); push 1, push 2, pop -> 2, push 2, push 3, push 4 (ignored)
#            increment(5, 100), increment(2, 100)
#            pop -> 103, pop -> 202, pop -> 201, pop -> -1
#
# The big idea (lazy increments - carry extra state):
#   A loop in increment costs O(k). Instead keep a parallel list 'inc':
#     increment(k, v): just do inc[top_of_those_k] += v   (O(1))
#     pop(): the real value is stack[i] + inc[i]. Before leaving, hand
#            inc[i] down to inc[i-1] - everything below was also part of
#            that increment.
#   Same "second list riding alongside the stack" idea as Min Stack.
# ============================================================


class CustomStackBrute:
    def __init__(self, maxSize):
        self.max_size = maxSize
        self.stack = []

    def push(self, x):
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def increment(self, k, val):
        limit = k if k < len(self.stack) else len(self.stack)
        for i in range(limit):              # O(k) every time
            self.stack[i] += val


class CustomStack:
    def __init__(self, maxSize):
        self.max_size = maxSize
        self.stack = []
        self.inc = []                       # pending increments, one per slot

    def push(self, x):
        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        i = len(self.stack) - 1
        bonus = self.inc.pop()
        if i > 0:
            self.inc[i - 1] += bonus        # pass the bonus down to the one below
        return self.stack.pop() + bonus

    def increment(self, k, val):
        if len(self.stack) == 0:
            return
        top_index = (k if k < len(self.stack) else len(self.stack)) - 1
        self.inc[top_index] += val          # mark it once, apply it lazily on pop


if __name__ == "__main__":
    cs = CustomStack(3)
    cs.push(1); cs.push(2)
    print(cs.pop())                 # 2
    cs.push(2); cs.push(3); cs.push(4)
    cs.increment(5, 100)
    cs.increment(2, 100)
    print(cs.pop())                 # 103
    print(cs.pop())                 # 202
    print(cs.pop())                 # 201
    print(cs.pop())                 # -1
