# ============================================================
# Day 18 - PRIMARY: Reverse Words in a String III  (LeetCode 557)
# ============================================================
# The question:
#   Reverse the letters of each word, but keep the words in the same
#   order and keep the single spaces where they are.
#
#   Example: "Let's take LeetCode contest" -> "s'teL ekat edoCteeL tsetnoc"
#
# The big idea (tokenize while walking + Day 9 swap):
#   Turn the string into a list of chars. Walk it with an index. A word
#   starts at 'start' and ends just before a space (or the end).
#   Each time a word ends, reverse that slice IN PLACE with the Day 9
#   two-pointer swap. One pass, no split(), no [::-1].
# ============================================================


def swap_reverse(chars, left, right):
    # The Day 9 loop: swap the ends, walk inward.
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


def reverse_words_brute(s):
    # Brute force: split into words, build each reversed word char by char, join.
    out = []
    for w in s.split(" "):
        rev = []
        for i in range(len(w) - 1, -1, -1):
            rev.append(w[i])
        out.append("".join(rev))
    return " ".join(out)


def reverse_words(s):
    chars = list(s)
    start = 0

    for i in range(len(chars) + 1):
        at_end = (i == len(chars))
        if at_end or chars[i] == " ":
            swap_reverse(chars, start, i - 1)   # word is chars[start .. i-1]
            start = i + 1                       # the next word begins after the space

    return "".join(chars)


if __name__ == "__main__":
    print(reverse_words("Let's take LeetCode contest"))   # s'teL ekat edoCteeL tsetnoc
    print(reverse_words("Mr Ding"))                        # rM gniD
    print(reverse_words_brute("hello"))                    # olleh
