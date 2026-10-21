# ============================================================
# Day 8 - VARIANT: Reverse Only Letters  (LeetCode 917)
# ============================================================
# The question:
#   Reverse the English letters in the string, but every non-letter
#   (dash, digit, symbol) must stay exactly where it is.
#
#   Example: "ab-cd"              -> "dc-ba"
#            "Test1ng-Leet=code-Q!" -> "Qedo1ct-eeLg=ntse-T!"
#
# The big idea (two pointers that skip non-letters):
#   Strings can't be changed in Python, so copy into a list first.
#   Two pointers from the ends. If either one is on a non-letter,
#   step past it. When both are on letters, swap and move inward.
# ============================================================


def reverse_only_letters_brute(s):
    # Brute force: collect letters, then refill them from the back.
    letters = []
    for ch in s:
        if ch.isalpha():
            letters.append(ch)
    result = []
    for ch in s:
        if ch.isalpha():
            result.append(letters.pop())    # pop gives letters in reverse order
        else:
            result.append(ch)
    return "".join(result)


def reverse_only_letters(s):
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        if not chars[left].isalpha():
            left += 1                       # not a letter, leave it alone
        elif not chars[right].isalpha():
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]   # swap the two letters
            left += 1
            right -= 1

    return "".join(chars)


if __name__ == "__main__":
    print(reverse_only_letters("ab-cd"))                  # dc-ba
    print(reverse_only_letters("a-bC-dEf-ghIj"))          # j-Ih-gfE-dCba
    print(reverse_only_letters("Test1ng-Leet=code-Q!"))   # Qedo1ct-eeLg=ntse-T!
