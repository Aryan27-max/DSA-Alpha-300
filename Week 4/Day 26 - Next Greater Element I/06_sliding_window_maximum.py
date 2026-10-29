# ============================================================
# Day 26 - VARIANT: Sliding Window Maximum  (LeetCode 239 - Hard)
# ============================================================
# The question:
#   Return the maximum of every window of size k.
#
#   Example: nums = [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]
#
# Today's angle - the monotonic DEQUE (rolling max):
#   Day 25 used two max-stacks. Today, the classic way.
#   Keep indexes whose values go DOWN from front to back.
#   - New number x arrives: pop from the BACK every index with value <= x.
#     They can never be the max again - x is bigger AND will stay longer.
#   - Pop from the FRONT if that index has slid out of the window.
#   - The front is always the current max.
#
#   No collections.deque: we build it from a list + a 'head' pointer.
#     back  = list[-1]   (append / pop from the end, like a stack)
#     front = list[head] (instead of deleting from the front, move head forward)
#   (Day 28 swaps this for a fixed-size circular buffer.)
# ============================================================


def max_sliding_window_brute(nums, k):
    result = []
    for i in range(len(nums) - k + 1):
        best = nums[i]
        for j in range(i, i + k):
            if nums[j] > best:
                best = nums[j]
        result.append(best)
    return result


def max_sliding_window(nums, k):
    dq = []                 # indexes; dq[head:] is the live deque
    head = 0
    result = []

    for i in range(len(nums)):
        if head < len(dq) and dq[head] <= i - k:
            head += 1                               # front index left the window

        while len(dq) > head and nums[dq[-1]] <= nums[i]:
            dq.pop()                                # smaller values at the back are useless now

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[head]])           # front = max of this window

    return result


if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
    print(max_sliding_window([1, -1], 1))                      # [1, -1]
    print(max_sliding_window([7, 2, 4], 2))                    # [7, 4]
