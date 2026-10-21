# ============================================================
# Day 9 - VARIANT: Reverse Words in a String III  (LeetCode 557)
# ============================================================
# The question:
#   Reverse the characters inside each word, but keep the words in
#   their original order. Words are separated by single spaces.
#
#   Example: "Let's take LeetCode contest" -> "s'teL ekat edoCteeL tsetnoc"
#
# The big idea:
#   Walk through a char list. Whenever a word ends (we hit a space or
#   the end of the string), reverse just that word with two pointers.
#   No splitting, no slicing - one pass.
# ============================================================


def reverse_words_brute(s):
    # Split into words, reverse each by reading it backwards, join back.
    words = s.split(" ")
    out = []
    for w in words:
        rev = []
        for i in range(len(w) - 1, -1, -1):
            rev.append(w[i])
        out.append("".join(rev))
    return " ".join(out)


def reverse_words(s):
    chars = list(s)
    n = len(chars)
    start = 0                           # where the current word begins

    for i in range(n + 1):
        if i == n or chars[i] == " ":
            # word runs from start to i - 1: reverse it in place
            left, right = start, i - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            start = i + 1               # next word starts after the space

    return "".join(chars)


if __name__ == "__main__":
    print(reverse_words("Let's take LeetCode contest"))   # s'teL ekat edoCteeL tsetnoc
    print(reverse_words("Mr Ding"))                        # rM gniD
