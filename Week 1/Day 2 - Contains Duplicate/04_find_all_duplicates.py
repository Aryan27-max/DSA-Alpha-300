# ============================================================
# Day 2 - VARIANT: Find All Duplicates in an Array  (LeetCode 442)
# ============================================================
# The question:
#   The list has n numbers, each between 1 and n. Every number shows up
#   once or twice. Return all the numbers that appear twice.
#   Do it in O(n) time and O(1) extra space.
#
#   Example: [4, 3, 2, 7, 8, 2, 3, 1] -> [2, 3]
#
# The big idea (array position marker):
#   Every value v points to a "home" index v - 1.
#   When we visit v, flip nums[v-1] to negative to say "v has been seen".
#   If it's ALREADY negative, we've seen v before -> it's a duplicate.
# ============================================================


def find_duplicates_brute(nums):
    # Brute force-ish: count with a dict. O(n) time but O(n) space.
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    result = []
    for num in counts:
        if counts[num] == 2:
            result.append(num)
    return result


def find_duplicates(nums):
    result = []

    for i in range(len(nums)):
        value = abs(nums[i])            # abs because we might have flipped it already
        home = value - 1

        if nums[home] < 0:
            result.append(value)        # home was already marked -> second time we see value
        else:
            nums[home] = -nums[home]    # mark: "value has been seen once"

    return result


if __name__ == "__main__":
    print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))   # [2, 3]
    print(find_duplicates([1, 1, 2]))                  # [1]
    print(find_duplicates([1]))                        # []
