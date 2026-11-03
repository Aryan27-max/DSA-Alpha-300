# ============================================================
# Day 30 - VARIANT: Rotate Array  (LeetCode 189)
# ============================================================
# The question:
#   Rotate nums to the RIGHT by k steps, in place.
#
#   Example: nums = [1,2,3,4,5,6,7], k = 3 -> [5,6,7,1,2,3,4]
#
# The big idea (reverse three times - O(1) extra space):
#   k may be bigger than n, so first do k = k % n.
#   1. Reverse the whole array        [7,6,5,4,3,2,1]
#   2. Reverse the first k elements   [5,6,7,4,3,2,1]
#   3. Reverse the rest               [5,6,7,1,2,3,4]
#   Every reverse is the Day 9 two-pointer swap.
#   (Same "reverse everything, then the parts" trick as Reverse Words.)
# ============================================================


def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def rotate_brute(nums, k):
    # Brute force: rotate by one step, k times. O(n * k).
    n = len(nums)
    k %= n
    for _ in range(k):
        last = nums[n - 1]
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last


def rotate_extra_array(nums, k):
    # Each element goes to (i + k) % n. O(n) time, O(n) extra space.
    n = len(nums)
    moved = [0] * n
    for i in range(n):
        moved[(i + k) % n] = nums[i]
    for i in range(n):
        nums[i] = moved[i]


def rotate(nums, k):
    n = len(nums)
    k %= n
    reverse(nums, 0, n - 1)     # whole thing
    reverse(nums, 0, k - 1)     # first k
    reverse(nums, k, n - 1)     # the rest


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    rotate(a, 3)
    print(a)        # [5, 6, 7, 1, 2, 3, 4]

    b = [-1, -100, 3, 99]
    rotate(b, 2)
    print(b)        # [3, 99, -1, -100]

    c = [1, 2]
    rotate(c, 5)
    print(c)        # [2, 1]
