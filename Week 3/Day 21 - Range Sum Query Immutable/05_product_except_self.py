# ============================================================
# Day 21 - VARIANT: Product of Array Except Self  (LeetCode 238)
# ============================================================
# The question:
#   Return answer where answer[i] = product of every number EXCEPT nums[i].
#   No division allowed, O(n) time.
#
#   Example: [1,2,3,4] -> [24,12,8,6]
#
# The big idea (prefix + suffix products):
#   answer[i] = (product of everything LEFT of i) * (product of everything RIGHT of i).
#   Pass 1 (left to right): answer[i] = product of nums[0..i-1].
#   Pass 2 (right to left): carry a running 'right' product and multiply
#   it into answer[i].
#   Extra space is O(1) - the output array doesn't count.
#   (Division would break on zeros anyway.)
# ============================================================


def product_except_self_brute(nums):
    # Brute force: multiply everything except i, for every i.
    n = len(nums)
    result = []
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p *= nums[j]
        result.append(p)
    return result


def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    left = 1
    for i in range(n):
        answer[i] = left            # product of everything before i
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right          # times product of everything after i
        right *= nums[i]

    return answer


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))          # [24, 12, 8, 6]
    print(product_except_self([-1, 1, 0, -3, 3]))     # [0, 0, 9, 0, 0]
