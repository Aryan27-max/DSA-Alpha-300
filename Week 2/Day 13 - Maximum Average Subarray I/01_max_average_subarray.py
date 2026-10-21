# ============================================================
# Day 13 - PRIMARY: Maximum Average Subarray I  (LeetCode 643)
# ============================================================
# The question:
#   Find the contiguous subarray of EXACTLY length k with the biggest
#   average, and return that average.
#
#   Example: nums = [1,12,-5,-6,50,3], k = 4 -> 12.75
#            (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
#
# The big idea (fixed-size sliding window):
#   Same length every time, so the biggest average = the biggest SUM.
#   Add up the first k numbers. Then slide the window one step right:
#     new sum = old sum + the number coming in - the number going out.
#   Each slide is O(1), so the whole thing is O(n).
#   (No sum(nums[i:i+k]) inside the loop - that's O(n*k).)
# ============================================================


def find_max_average_brute(nums, k):
    # Brute force: re-add every window from scratch.
    best = None
    for i in range(len(nums) - k + 1):
        s = 0
        for j in range(i, i + k):
            s += nums[j]
        if best is None or s > best:
            best = s
    return best / k


def find_max_average(nums, k):
    window = 0
    for i in range(k):
        window += nums[i]               # sum of the very first window

    best = window
    for i in range(k, len(nums)):
        window += nums[i]               # number entering on the right
        window -= nums[i - k]           # number leaving on the left
        if window > best:
            best = window

    return best / k                     # divide once at the end


if __name__ == "__main__":
    print(find_max_average([1, 12, -5, -6, 50, 3], 4))        # 12.75
    print(find_max_average([5], 1))                           # 5.0
    print(find_max_average_brute([1, 12, -5, -6, 50, 3], 4))  # 12.75
