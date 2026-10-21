# ============================================================
# Day 9 - VARIANT: Reverse Prefix of Word  (LeetCode 2000)
# ============================================================
# The question:
#   Find the FIRST occurrence of character ch in word. Reverse the part
#   of the word from index 0 up to and including that position.
#   If ch isn't in the word, return the word unchanged.
#
#   Example: word = "abcdefd", ch = "d" -> "dcbaefd"
#
# The big idea:
#   Scan for ch. Once found at index i, run the two-pointer swap on [0, i].
# ============================================================


def reverse_prefix_brute(word, ch):
    # Build the answer: prefix read backwards + the rest as-is.
    for i in range(len(word)):
        if word[i] == ch:
            out = []
            for j in range(i, -1, -1):
                out.append(word[j])
            for j in range(i + 1, len(word)):
                out.append(word[j])
            return "".join(out)
    return word


def reverse_prefix(word, ch):
    stop = -1
    for i in range(len(word)):
        if word[i] == ch:
            stop = i                    # first place ch shows up
            break

    if stop == -1:
        return word                     # ch not found, nothing to do

    chars = list(word)
    left, right = 0, stop
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


if __name__ == "__main__":
    print(reverse_prefix("abcdefd", "d"))   # dcbaefd
    print(reverse_prefix("xyxzxe", "z"))    # zxyxxe
    print(reverse_prefix("abcd", "z"))      # abcd
