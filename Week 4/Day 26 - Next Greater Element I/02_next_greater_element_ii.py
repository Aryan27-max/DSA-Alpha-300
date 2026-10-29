# ============================================================
# Day 26 - VARIANT: Next Greater Element II  (LeetCode 503)
# ============================================================
# The question:
#   nums is CIRCULAR (after the last element comes the first again).
#   For every element, return the next greater number when walking
#   forward (wrapping around), or -1. Values may repeat.
#
#   Example: [1,2,1] -> [2,-1,2]    (the last 1 wraps around to find 2)
#            [1,2,3,4,3] -> [2,3,4,-1,4]
#
# The big idea (circular array = walk it twice):
#   Pretend the array is written out twice: [1,2,1,1,2,1].
#   Loop i from 0 to 2n-1 and use nums[i % n].
#   Store INDEXES in the stack (values can repeat, so a value->answer
#   dict wouldn't work). Only push during the first pass - the second
#   pass is just there to answer whoever is still waiting.
# ============================================================


def next_greater_elements_brute(nums):
    n = len(nums)
    result = []
    for i in range(n):
        answer = -1
        for step in range(1, n):
            j = (i + step) % n          # walk forward with wrap-around
            if nums[j] > nums[i]:
                answer = nums[j]
                break
        result.append(answer)
    return result


def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []                          # indexes still waiting

    for i in range(2 * n):
        x = nums[i % n]
        while len(stack) > 0 and nums[stack[-1]] < x:
            result[stack.pop()] = x
        if i < n:
            stack.append(i)             # only real positions wait for answers

    return result


if __name__ == "__main__":
    print(next_greater_elements([1, 2, 1]))          # [2, -1, 2]
    print(next_greater_elements([1, 2, 3, 4, 3]))    # [2, 3, 4, -1, 4]
    print(next_greater_elements([5, 5, 5]))          # [-1, -1, -1]
