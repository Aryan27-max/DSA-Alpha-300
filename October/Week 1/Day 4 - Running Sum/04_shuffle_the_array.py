# ============================================================
# Day 4 - VARIANT: Shuffle the Array  (LeetCode 1470)
# ============================================================
# The question:
#   nums looks like [x1, x2, ..., xn, y1, y2, ..., yn].
#   Return it as [x1, y1, x2, y2, ..., xn, yn].
#
#   Example: nums = [2, 5, 1, 3, 4, 7], n = 3 -> [2, 3, 5, 4, 1, 7]
#
# The big idea:
#   x_i lives at index i, and its partner y_i lives at index i + n.
#   Walk i from 0 to n-1 and append both.
# ============================================================


def shuffle_brute(nums, n):
    # "Brute" version: split into two lists first, then zip them by hand.
    xs = []
    ys = []
    for i in range(n):
        xs.append(nums[i])
    for i in range(n, 2 * n):
        ys.append(nums[i])
    result = []
    for i in range(n):
        result.append(xs[i])
        result.append(ys[i])
    return result


def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])          # x_i from the first half
        result.append(nums[i + n])      # y_i from the second half
    return result


if __name__ == "__main__":
    print(shuffle([2, 5, 1, 3, 4, 7], 3))         # [2, 3, 5, 4, 1, 7]
    print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))   # [1, 4, 2, 3, 3, 2, 4, 1]
