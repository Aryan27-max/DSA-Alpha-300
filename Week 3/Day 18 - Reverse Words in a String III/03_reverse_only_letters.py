# ============================================================
# Day 18 - VARIANT: Reverse Only Letters  (LeetCode 917)
# ============================================================
# The question:
#   Reverse only the English letters. Every non-letter stays at its index.
#
#   Example: "a-bC-dEf-ghIj" -> "j-Ih-gfE-dCba"
#
# The big idea (reverse while ignoring non-alpha):
#   The Day 9 swap loop, with one extra rule: if a pointer is on a
#   non-letter, step past it instead of swapping.
#   We check "is it a letter?" with ASCII ranges here (A-Z is 65-90,
#   a-z is 97-122) so the idea works in any language.
# ============================================================


def is_letter(ch):
    code = ord(ch)
    return (65 <= code <= 90) or (97 <= code <= 122)


def reverse_only_letters_brute(s):
    # Brute force: pull the letters out, then pop them back in reverse.
    letters = []
    for ch in s:
        if is_letter(ch):
            letters.append(ch)
    out = []
    for ch in s:
        out.append(letters.pop() if is_letter(ch) else ch)
    return "".join(out)


def reverse_only_letters(s):
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        if not is_letter(chars[left]):
            left += 1
        elif not is_letter(chars[right]):
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)


if __name__ == "__main__":
    print(reverse_only_letters("ab-cd"))                  # dc-ba
    print(reverse_only_letters("a-bC-dEf-ghIj"))          # j-Ih-gfE-dCba
    print(reverse_only_letters("Test1ng-Leet=code-Q!"))   # Qedo1ct-eeLg=ntse-T!
