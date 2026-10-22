# ============================================================
# Day 18 - VARIANT: Reverse Words in a String  (LeetCode 151)
# ============================================================
# The question:
#   Reverse the ORDER of the words. Remove leading/trailing spaces and
#   squeeze multiple spaces between words into one.
#
#   Example: "  hello world  " -> "world hello"
#            "a good   example" -> "example good a"
#
# The big idea ("reverse everything, then reverse the parts"):
#   1. Copy into a list of chars with clean spacing (read/write pointer).
#   2. Reverse the whole list            -> "dlrow olleh"
#   3. Reverse every word on its own     -> "world hello"
#   Step 3 is literally today's primary.
# ============================================================


def swap_reverse(chars, left, right):
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


def reverse_words_brute(s):
    # Brute force: split(), then build a new list from the last word to the first.
    words = s.split()
    out = []
    for i in range(len(words) - 1, -1, -1):
        out.append(words[i])
    return " ".join(out)


def reverse_words(s):
    # Step 1: clean spacing
    chars = []
    for ch in s:
        if ch != " ":
            chars.append(ch)
        elif len(chars) > 0 and chars[-1] != " ":
            chars.append(" ")           # only one space after a word
    if len(chars) > 0 and chars[-1] == " ":
        chars.pop()                     # no trailing space

    # Step 2: reverse the whole thing
    swap_reverse(chars, 0, len(chars) - 1)

    # Step 3: reverse each word back (today's primary)
    start = 0
    for i in range(len(chars) + 1):
        if i == len(chars) or chars[i] == " ":
            swap_reverse(chars, start, i - 1)
            start = i + 1

    return "".join(chars)


if __name__ == "__main__":
    print(reverse_words("the sky is blue"))     # blue is sky the
    print(reverse_words("  hello world  "))     # world hello
    print(reverse_words("a good   example"))    # example good a
