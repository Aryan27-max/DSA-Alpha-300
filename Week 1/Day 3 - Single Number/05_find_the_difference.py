# ============================================================
# Day 3 - VARIANT: Find the Difference  (LeetCode 389)
# ============================================================
# The question:
#   String t is string s shuffled, with ONE extra letter added somewhere.
#   Return that extra letter.
#
#   Example: s = "abcd", t = "abcde" -> "e"
#
# The big idea (XOR on characters):
#   Turn each character into its number with ord().
#   XOR every character of s and t together. Every letter in s also
#   appears in t, so those cancel. The extra letter is left over.
# ============================================================


def find_the_difference_brute(s, t):
    # Counting version: count letters in s, then use them up while reading t.
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if counts.get(ch, 0) == 0:
            return ch               # t has a letter s doesn't have (or has one more)
        counts[ch] -= 1
    return ""


def find_the_difference(s, t):
    x = 0
    for ch in s:
        x ^= ord(ch)
    for ch in t:
        x ^= ord(ch)
    return chr(x)                   # convert the leftover number back to a letter


if __name__ == "__main__":
    print(find_the_difference("abcd", "abcde"))   # e
    print(find_the_difference("", "y"))           # y
    print(find_the_difference("aab", "abaa"))     # a
