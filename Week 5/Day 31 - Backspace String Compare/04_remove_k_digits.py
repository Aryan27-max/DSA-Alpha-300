# ============================================================
# Day 31 - VARIANT: Remove K Digits  (LeetCode 402)
# ============================================================
# The question:
#   num is a string of digits. Remove exactly k digits so the remaining
#   number is as SMALL as possible. Return it as a string with no leading
#   zeros ("0" if nothing is left).
#
#   Example: num = "1432219", k = 3 -> "1219"
#            num = "10200",   k = 1 -> "200"
#            num = "10",      k = 2 -> "0"
#
# The big idea (greedy with a monotonic increasing stack):
#   The leftmost digits matter most. If a digit is bigger than the digit
#   right after it, removing it makes the number smaller.
#   Walk the digits with a stack:
#     while k > 0 and the top is bigger than the new digit: pop it, k -= 1
#     push the new digit
#   If k is still > 0 at the end, the stack is increasing - remove from
#   the END (the biggest digits). Then strip leading zeros.
#   Same "pop while the new value beats the top" move as Day 26.
# ============================================================


def remove_k_digits_brute(num, k):
    # Brute force: k times, try removing each digit and keep the smallest result.
    # (Equal-length digit strings compare correctly as strings.)
    current = num
    for _ in range(k):
        best = None
        for i in range(len(current)):
            candidate = current[:i] + current[i + 1:]
            if best is None or candidate < best:
                best = candidate
        current = best
    i = 0
    while i < len(current) - 1 and current[i] == "0":
        i += 1
    result = current[i:]
    return result if result != "" else "0"


def remove_k_digits(num, k):
    stack = []
    for d in num:
        while k > 0 and len(stack) > 0 and stack[-1] > d:
            stack.pop()                 # a bigger digit before a smaller one - drop it
            k -= 1
        stack.append(d)

    while k > 0:
        stack.pop()                     # still need removals: drop from the end
        k -= 1

    start = 0
    while start < len(stack) and stack[start] == "0":
        start += 1                      # skip leading zeros
    if start == len(stack):
        return "0"
    return "".join(stack[start:])


if __name__ == "__main__":
    print(remove_k_digits("1432219", 3))          # 1219
    print(remove_k_digits("10200", 1))            # 200
    print(remove_k_digits("10", 2))               # 0
    print(remove_k_digits("112", 1))              # 11
    print(remove_k_digits_brute("1432219", 3))    # 1219
