# ============================================================
# Day 25 - VARIANT: Sliding Window Maximum  (LeetCode 239 - Hard)
# ============================================================
# The question:
#   A window of size k slides from left to right over nums. Return the
#   maximum inside the window at every position.
#
#   Example: nums = [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]
#
# Today's angle - a "max queue" built from two MAX STACKS:
#   (You'll see this problem again on Day 26 and Day 28 with other tools.)
#   A window is a queue: new number in at the back, oldest out at the front.
#   Min Stack taught us a stack that knows its min/max in O(1).
#   Day 27 will teach that two stacks make a queue. Put them together:
#     in_stack  - receives new numbers. Each entry stores (value, max so far).
#     out_stack - serves the front. Each entry stores (value, max so far).
#     When out_stack is empty and we need to remove, pour in_stack into it
#     (recomputing the running max as we go).
#     Window max = the bigger of the two tops' running maxes.
#   Every number moves at most twice -> amortized O(1) per step, O(n) total.
# ============================================================


def max_sliding_window_brute(nums, k):
    # Brute force: scan every window.
    result = []
    for i in range(len(nums) - k + 1):
        best = nums[i]
        for j in range(i, i + k):
            if nums[j] > best:
                best = nums[j]
        result.append(best)
    return result


class MaxQueue:
    def __init__(self):
        self.in_stack = []          # (value, max of in_stack up to here)
        self.out_stack = []         # (value, max of out_stack up to here)

    def push(self, v):
        if len(self.in_stack) == 0 or v > self.in_stack[-1][1]:
            self.in_stack.append((v, v))
        else:
            self.in_stack.append((v, self.in_stack[-1][1]))

    def pop(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:          # pour: oldest ends up on top
                v = self.in_stack.pop()[0]
                if len(self.out_stack) == 0 or v > self.out_stack[-1][1]:
                    self.out_stack.append((v, v))
                else:
                    self.out_stack.append((v, self.out_stack[-1][1]))
        self.out_stack.pop()

    def get_max(self):
        if len(self.in_stack) == 0:
            return self.out_stack[-1][1]
        if len(self.out_stack) == 0:
            return self.in_stack[-1][1]
        a, b = self.in_stack[-1][1], self.out_stack[-1][1]
        return a if a > b else b


def max_sliding_window(nums, k):
    q = MaxQueue()
    result = []
    for i in range(len(nums)):
        q.push(nums[i])
        if i >= k:
            q.pop()                         # nums[i - k] leaves the window
        if i >= k - 1:
            result.append(q.get_max())
    return result


if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
    print(max_sliding_window([1], 1))                          # [1]
    print(max_sliding_window([9, 8, 7, 6], 2))                 # [9, 8, 7]
