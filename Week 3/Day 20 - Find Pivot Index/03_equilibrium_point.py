# ============================================================
# Day 20 - VARIANT: Equilibrium Point  (GeeksforGeeks)
# ============================================================
# The question:
#   Return the equilibrium point - a position where the sum of elements
#   before it equals the sum after it. GFG wants a 1-BASED position
#   (and -1 if there isn't one). Recent versions ask for 0-based; we
#   return both so you can match whichever your judge wants.
#
#   Example: [1, 3, 5, 2, 2] -> position 3 (1-based), index 2 (0-based)
#            1 + 3 = 4 = 2 + 2
#
# The big idea (prefix + suffix view, just for variety):
#   Same total/left trick works. Here's another way to see it, using a
#   prefix array and a suffix array:
#     prefix[i] = sum of nums[0..i-1]
#     suffix[i] = sum of nums[i+1..n-1]
#   That's O(n) space - the primary's version is O(1). Both are O(n) time.
# ============================================================


def equilibrium_point_prefix_suffix(arr):
    n = len(arr)
    prefix = [0] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i - 1]      # sum of everything before i
    suffix = [0] * n
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i + 1]      # sum of everything after i
    for i in range(n):
        if prefix[i] == suffix[i]:
            return i + 1                            # 1-based
    return -1


def equilibrium_point(arr):
    total = 0
    for x in arr:
        total += x

    left = 0
    for i in range(len(arr)):
        if left == total - left - arr[i]:
            return i + 1                            # 1-based (GFG classic)
        left += arr[i]
    return -1


if __name__ == "__main__":
    print(equilibrium_point([1, 3, 5, 2, 2]))                 # 3
    print(equilibrium_point([1]))                             # 1
    print(equilibrium_point([1, 2, 3]))                       # -1
    print(equilibrium_point_prefix_suffix([1, 3, 5, 2, 2]))   # 3
