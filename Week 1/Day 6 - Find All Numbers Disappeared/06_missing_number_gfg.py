# ============================================================
# Day 6 - VARIANT: Missing number in array  (GeeksforGeeks)
# ============================================================
# The question:
#   You get n - 1 distinct numbers from the range 1..n (note: starts
#   at 1, not 0). One number is missing. Find it.
#
#   Example: n = 5, arr = [1, 2, 3, 5] -> 4
#
# The big idea:
#   XOR 1..n with every value in the array. Present numbers cancel,
#   the missing one stays. XOR also avoids overflow worries that the
#   sum formula has in languages like C++/Java (Python is fine either way).
# ============================================================


def missing_number_sum(arr):
    # Sum formula version: total of 1..n minus what's there.
    n = len(arr) + 1
    total = n * (n + 1) // 2
    for num in arr:
        total -= num
    return total


def missing_number(arr):
    n = len(arr) + 1
    x = 0
    for v in range(1, n + 1):
        x ^= v                  # XOR in every number that SHOULD be there
    for num in arr:
        x ^= num                # XOR in every number that IS there
    return x                    # only the missing one is left


if __name__ == "__main__":
    print(missing_number([1, 2, 3, 5]))                     # 4
    print(missing_number([6, 1, 2, 8, 3, 4, 7, 10, 5]))     # 9
    print(missing_number_sum([1]))                          # 2
