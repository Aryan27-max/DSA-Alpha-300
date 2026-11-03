# ============================================================
# Day 26 - PRIMARY: Next Greater Element I  (LeetCode 496)
# ============================================================
# The question:
#   nums1 is a subset of nums2 (all values distinct). For each x in nums1,
#   find x in nums2 and return the first number to its RIGHT that is
#   bigger than x, or -1 if there isn't one.
#
#   Example: nums1 = [4,1,2], nums2 = [1,3,4,2] -> [-1,3,-1]
#            4: nothing bigger after it   1: next bigger is 3   2: nothing after
#
# The big idea (monotonic decreasing stack):
#   Walk nums2 once with a stack of numbers that are still WAITING for
#   their next greater element. Those waiting numbers always go DOWN from
#   bottom to top (a bigger number would have already "answered" them).
#   For each new number x:
#     while the top is smaller than x: x IS the top's next greater -> record it, pop
#     then push x (now x waits too)
#   Anything left in the stack at the end never found one -> -1.
#   Save the answers in a dict, then just look up each nums1 value.
#   Each number is pushed once and popped once -> O(n).
# ============================================================


def next_greater_element_brute(nums1, nums2):
    # Brute force: find x in nums2, then scan to its right.
    result = []
    for x in nums1:
        pos = 0
        while nums2[pos] != x:
            pos += 1
        answer = -1
        for j in range(pos + 1, len(nums2)):
            if nums2[j] > x:
                answer = nums2[j]
                break
        result.append(answer)
    return result


def next_greater_element(nums1, nums2):
    next_greater = {}               # value -> its next greater value in nums2
    stack = []                      # values still waiting (decreasing upward)

    for x in nums2:
        while len(stack) > 0 and stack[-1] < x:
            next_greater[stack.pop()] = x   # x is the first bigger number after it
        stack.append(x)

    result = []
    for x in nums1:
        result.append(next_greater.get(x, -1))
    return result


if __name__ == "__main__":
    print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))         # [-1, 3, -1]
    print(next_greater_element([2, 4], [1, 2, 3, 4]))            # [3, -1]
    print(next_greater_element_brute([4, 1, 2], [1, 3, 4, 2]))   # [-1, 3, -1]
