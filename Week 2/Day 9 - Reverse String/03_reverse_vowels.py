# ============================================================
# Day 9 - VARIANT: Reverse Vowels of a String  (LeetCode 345)
# ============================================================
# The question:
#   Reverse only the vowels (a, e, i, o, u - upper or lower case).
#   Everything else stays where it is.
#
#   Example: "IceCreAm" -> "AceCreIm"     "leetcode" -> "leotcede"
#
# The big idea:
#   Same as Reverse Only Letters (Day 8), but the "skip" rule is
#   "not a vowel". Use a set for O(1) vowel checks.
# ============================================================

VOWELS = set("aeiouAEIOU")


def reverse_vowels_brute(s):
    # Collect vowels, then put them back popping from the end.
    found = []
    for ch in s:
        if ch in VOWELS:
            found.append(ch)
    result = []
    for ch in s:
        if ch in VOWELS:
            result.append(found.pop())
        else:
            result.append(ch)
    return "".join(result)


def reverse_vowels(s):
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        if chars[left] not in VOWELS:
            left += 1               # left isn't a vowel, keep looking
        elif chars[right] not in VOWELS:
            right -= 1              # right isn't a vowel, keep looking
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)


if __name__ == "__main__":
    print(reverse_vowels("IceCreAm"))   # AceCreIm
    print(reverse_vowels("leetcode"))   # leotcede
    print(reverse_vowels("hello"))      # holle
