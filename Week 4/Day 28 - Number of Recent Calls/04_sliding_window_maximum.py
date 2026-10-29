# ============================================================
# Day 28 - VARIANT: Sliding Window Maximum  (LeetCode 239 - Hard)
# ============================================================
# The question:
#   Return the maximum of every window of size k.
#
#   Example: nums = [1,3,-1,-3,5,3,6,7], k = 3 -> [3,3,5,5,6,7]
#
# Today's angle - monotonic deque in a FIXED-SIZE CIRCULAR BUFFER:
#   Day 25: two max-stacks.  Day 26: monotonic deque in a list + head
#   (that list kept growing). Today: the same monotonic deque, but stored
#   in a ring of exactly k slots, like Design Circular Deque (Day 27).
#   Why k slots is enough: after removing the expired front, every index
#   left is inside the current window, so there are at most k of them.
#     front = buf[head]
#     back  = buf[(head + size - 1) % k]
#   Memory is O(k) instead of O(n).
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
    buf = [0] * k               # ring of indexes
    head = 0
    size = 0
    result = []

    for i in range(len(nums)):
        if size > 0 and buf[head] <= i - k:
            head = (head + 1) % k               # pop front: it left the window
            size -= 1

        while size > 0 and nums[buf[(head + size - 1) % k]] <= nums[i]:
            size -= 1                           # pop back: smaller and older

        buf[(head + size) % k] = i              # push back
        size += 1

        if i >= k - 1:
            result.append(nums[buf[head]])      # front = window max

    return result


if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
    print(max_sliding_window([4, 2, 12, 3], 1))                # [4, 2, 12, 3]
    print(max_sliding_window([1, 3, 1, 2, 0, 5], 3))           # [3, 3, 2, 5]
