# ============================================================
# Day 2 - VARIANT: Duplicate Zeros  (LeetCode 1089)
# ============================================================
# The question:
#   Every time you see a 0, write it twice and shift everything else
#   to the right. The array keeps its length, so stuff falls off the end.
#   Modify the list IN PLACE, return nothing.
#
#   Example: [1, 0, 2, 3, 0, 4, 5, 0] -> [1, 0, 0, 2, 3, 0, 0, 4]
#
# The big idea:
#   Shifting right one by one is slow. Instead:
#   1. Count zeros. Pretend the array is longer by that many slots.
#   2. Walk BACKWARDS with two pointers:
#        i = position in the original array
#        j = position in the imaginary longer array
#      Copy arr[i] to arr[j] (only if j is inside the real array).
#      If arr[i] is 0, write an extra 0.
#   Going backwards means we never overwrite something we still need.
# ============================================================


def duplicate_zeros_brute(arr):
    # Brute force: whenever we see a 0, shift everything right by one.
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:
            # shift right, starting from the end
            for k in range(n - 1, i, -1):
                arr[k] = arr[k - 1]
            i += 2              # skip the zero we just duplicated
        else:
            i += 1


def duplicate_zeros(arr):
    n = len(arr)

    zeros = 0
    for num in arr:
        if num == 0:
            zeros += 1

    i = n - 1               # last index of the real array
    j = n - 1 + zeros       # last index of the imaginary stretched array

    while i >= 0 and j >= 0:
        if j < n:
            arr[j] = arr[i]         # copy only if j lands inside the real array

        if arr[i] == 0:
            j -= 1                  # zero gets a second copy
            if j < n:
                arr[j] = 0

        i -= 1
        j -= 1


if __name__ == "__main__":
    a = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros(a)
    print(a)                        # [1, 0, 0, 2, 3, 0, 0, 4]

    b = [1, 2, 3]
    duplicate_zeros(b)
    print(b)                        # [1, 2, 3]

    c = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_zeros_brute(c)
    print(c)                        # [1, 0, 0, 2, 3, 0, 0, 4]
