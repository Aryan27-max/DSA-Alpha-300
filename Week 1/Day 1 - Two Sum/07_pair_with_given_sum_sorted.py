# ============================================================
# Day 1 - VARIANT: Pair with given sum in sorted array  (GeeksforGeeks)
# ============================================================
# The question:
#   Given a SORTED array (it can have duplicates) and a target,
#   COUNT how many pairs (i < j) have arr[i] + arr[j] == target.
#
#   Example: arr = [-1, 1, 5, 5, 7], target = 6  ->  3
#            pairs: (-1, 7), (1, 5), (1, 5)
#
# The big idea:
#   Two pointers again. The tricky part is duplicates:
#   when we find a match, count how many copies of the left value
#   and right value there are, and multiply them.
#   Special case: if left value == right value, every pair inside that
#   block works, which is cnt * (cnt - 1) / 2.
# ============================================================


def count_pairs_brute(arr, target):
    # Brute force: check every pair.
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count


def count_pairs(arr, target):
    left, right = 0, len(arr) - 1
    count = 0

    while left < right:
        total = arr[left] + arr[right]

        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            # we found a matching pair of VALUES
            if arr[left] == arr[right]:
                # everything between left and right is the same number
                block = right - left + 1
                count += block * (block - 1) // 2
                break

            # count copies of the left value
            left_count = 1
            while left + 1 < right and arr[left + 1] == arr[left]:
                left += 1
                left_count += 1

            # count copies of the right value
            right_count = 1
            while right - 1 > left and arr[right - 1] == arr[right]:
                right -= 1
                right_count += 1

            count += left_count * right_count   # every left copy pairs with every right copy
            left += 1
            right -= 1

    return count


if __name__ == "__main__":
    print(count_pairs([-1, 1, 5, 5, 7], 6))        # 3
    print(count_pairs([1, 1, 1, 1], 2))            # 6
    print(count_pairs([-1, 10, 10, 12, 15], 125))  # 0
