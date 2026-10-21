# ============================================================
# Day 12 - PRIMARY: Squares of a Sorted Array  (LeetCode 977)
# ============================================================
# The question:
#   nums is sorted (it can have negatives). Return the squares of every
#   number, also sorted.
#
#   Example: [-4,-1,0,3,10] -> [0,1,9,16,100]
#
# The big idea (where is the biggest square?):
#   Negatives flip when squared: -4 squared (16) beats 3 squared (9).
#   So the BIGGEST square is always at one of the two ENDS, never in the
#   middle. Two pointers from the ends: compare absolute values, write the
#   bigger square into the result from the BACK, move that pointer inward.
#   That's O(n) - no sorting at all. (No sorted(x*x for x in nums).)
# ============================================================


def merge_sort(arr):
    # Our own merge sort, only used by the brute force.
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    while i < len(left):
        out.append(left[i]); i += 1
    while j < len(right):
        out.append(right[j]); j += 1
    return out


def sorted_squares_brute(nums):
    # Brute force: square everything, then sort it (our own sort). O(n log n).
    squares = []
    for x in nums:
        squares.append(x * x)
    return merge_sort(squares)


def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1

    for w in range(n - 1, -1, -1):          # fill from the biggest slot down
        if abs(nums[left]) > abs(nums[right]):
            result[w] = nums[left] * nums[left]
            left += 1
        else:
            result[w] = nums[right] * nums[right]
            right -= 1

    return result


if __name__ == "__main__":
    print(sorted_squares([-4, -1, 0, 3, 10]))        # [0, 1, 9, 16, 100]
    print(sorted_squares([-7, -3, 2, 3, 11]))        # [4, 9, 9, 49, 121]
    print(sorted_squares_brute([-5, -3, -2, -1]))    # [1, 4, 9, 25]
