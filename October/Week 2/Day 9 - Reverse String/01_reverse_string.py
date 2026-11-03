# ============================================================
# Day 9 - PRIMARY: Reverse String  (LeetCode 344)
# ============================================================
# The question:
#   You get a list of characters. Reverse it IN PLACE (don't make a new
#   list) using O(1) extra memory. Return nothing.
#
#   Example: ["h","e","l","l","o"] -> ["o","l","l","e","h"]
#
# The big idea (two-pointer swap):
#   Swap the first and last, then the second and second-last, and so on,
#   until the pointers meet in the middle. That's it - the lesson IS the loop.
#   (No s.reverse(), reversed(s), or s[::-1].)
#
#   Bonus: a recursive version, as a warm-up for November's recursion week.
#   It does the same swaps, but each call handles one pair and hands the
#   rest to the next call.
# ============================================================


def reverse_string_brute(s):
    # Brute force: copy into a new list from the back, then copy it over. O(n) space.
    temp = []
    for i in range(len(s) - 1, -1, -1):
        temp.append(s[i])
    for i in range(len(s)):
        s[i] = temp[i]


def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]   # swap the outer pair
        left += 1                               # move inward
        right -= 1


def reverse_string_recursive(s, left=0, right=None):
    # Same swaps, done recursively. Uses O(n) call-stack space.
    if right is None:
        right = len(s) - 1
    if left >= right:
        return                                  # base case: pointers met
    s[left], s[right] = s[right], s[left]
    reverse_string_recursive(s, left + 1, right - 1)


if __name__ == "__main__":
    a = ["h", "e", "l", "l", "o"]
    reverse_string(a)
    print(a)    # ['o', 'l', 'l', 'e', 'h']

    b = ["H", "a", "n", "n", "a", "h"]
    reverse_string_recursive(b)
    print(b)    # ['h', 'a', 'n', 'n', 'a', 'H']

    c = ["a", "b", "c"]
    reverse_string_brute(c)
    print(c)    # ['c', 'b', 'a']
