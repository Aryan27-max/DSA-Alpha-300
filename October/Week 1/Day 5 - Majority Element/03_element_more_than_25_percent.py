# ============================================================
# Day 5 - VARIANT: Element Appearing More Than 25% in Sorted Array  (LeetCode 1287)
# ============================================================
# The question:
#   The array is sorted. Exactly one number appears more than 25% of
#   the time. Return it.
#
#   Example: [1, 2, 2, 6, 6, 6, 6, 7, 10] -> 6
#
# The big idea:
#   Because it's sorted, copies sit next to each other in one block.
#   A block longer than n/4 MUST cover at least one of these spots:
#       n/4,  n/2,  3n/4
#   So only 3 candidates exist. For each one, use binary search to find
#   where its block starts and ends, and check the length.  -> O(log n)
#
#   Simpler O(n) way: if arr[i] == arr[i + n//4], that block is long enough.
# ============================================================


def find_special_integer_linear(arr):
    # O(n): the element at i and the one a quarter-length later are equal
    # only if that value fills more than 25% of the array.
    n = len(arr)
    quarter = n // 4
    for i in range(n - quarter):
        if arr[i] == arr[i + quarter]:
            return arr[i]
    return arr[0]


def first_index(arr, target):
    # Our own binary search: leftmost position of target.
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            if arr[mid] == target:
                ans = mid
            right = mid - 1         # keep looking left
        else:
            left = mid + 1
    return ans


def last_index(arr, target):
    # Our own binary search: rightmost position of target.
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            if arr[mid] == target:
                ans = mid
            left = mid + 1          # keep looking right
        else:
            right = mid - 1
    return ans


def find_special_integer(arr):
    n = len(arr)
    for pos in [n // 4, n // 2, (3 * n) // 4]:
        candidate = arr[pos]
        count = last_index(arr, candidate) - first_index(arr, candidate) + 1
        if count > n // 4:
            return candidate
    return arr[0]


if __name__ == "__main__":
    print(find_special_integer([1, 2, 2, 6, 6, 6, 6, 7, 10]))   # 6
    print(find_special_integer([1, 1]))                         # 1
    print(find_special_integer_linear([1, 2, 3, 3]))            # 3
