# ============================================================
# Day 5 - VARIANT: Majority Element  (GeeksforGeeks)
# ============================================================
# The question:
#   Same as LeetCode 169, BUT the majority is NOT guaranteed to exist.
#   Return the element that appears more than n/2 times, or -1 if none.
#
#   Example: [3, 1, 3, 3, 2] -> 3       [7] -> 7       [1, 2, 3] -> -1
#
# The big idea:
#   Boyer-Moore finds the only POSSIBLE majority.
#   Because it might not really be one, do a second pass to count it.
# ============================================================


def majority_element_brute(arr):
    # Hashmap counting.
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    for num in counts:
        if counts[num] > len(arr) // 2:
            return num
    return -1


def majority_element(arr):
    # Pass 1: Boyer-Moore voting to get a candidate
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    # Pass 2: make sure the candidate really is a majority
    actual = 0
    for num in arr:
        if num == candidate:
            actual += 1

    if actual > len(arr) // 2:
        return candidate
    return -1


if __name__ == "__main__":
    print(majority_element([3, 1, 3, 3, 2]))   # 3
    print(majority_element([7]))               # 7
    print(majority_element([2, 13]))           # -1
    print(majority_element([1, 2, 3]))         # -1
