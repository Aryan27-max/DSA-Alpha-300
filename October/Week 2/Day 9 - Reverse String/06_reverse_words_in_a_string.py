# ============================================================
# Day 9 - VARIANT: Reverse Words in a String  (LeetCode 151)
# ============================================================
# The question:
#   Reverse the ORDER of the words. The input may have leading/trailing
#   spaces and multiple spaces between words. The output must have
#   single spaces between words and no extra spaces at the ends.
#
#   Example: "  the sky is  blue " -> "blue is sky the"
#
# The big idea (the classic "reverse twice" trick):
#   1. Clean up spaces into a char list (single spaces, none at the ends).
#   2. Reverse the WHOLE list   -> "eulb si yks eht"
#   3. Reverse EACH word again  -> "blue is sky the"
#   Every step is just the two-pointer swap from today's primary.
# ============================================================


def reverse_range(chars, left, right):
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1


def reverse_words_brute(s):
    # Easy version: split (handles extra spaces), swap words with two pointers, join.
    words = s.split()
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return " ".join(words)


def reverse_words(s):
    # Step 1: copy into a list with clean spacing
    chars = []
    for ch in s:
        if ch != " ":
            chars.append(ch)
        elif len(chars) > 0 and chars[-1] != " ":
            chars.append(" ")               # keep only one space between words
    if len(chars) > 0 and chars[-1] == " ":
        chars.pop()                         # drop a trailing space

    # Step 2: reverse everything
    reverse_range(chars, 0, len(chars) - 1)

    # Step 3: reverse each word back to normal spelling
    start = 0
    for i in range(len(chars) + 1):
        if i == len(chars) or chars[i] == " ":
            reverse_range(chars, start, i - 1)
            start = i + 1

    return "".join(chars)


if __name__ == "__main__":
    print(reverse_words("the sky is blue"))        # blue is sky the
    print(reverse_words("  hello world  "))        # world hello
    print(reverse_words("a good   example"))       # example good a
