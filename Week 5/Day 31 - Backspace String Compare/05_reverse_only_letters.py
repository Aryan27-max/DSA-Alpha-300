# ============================================================
# Day 31 - VARIANT: Reverse Only Letters  (LeetCode 917)
# ============================================================
# The question:
#   Reverse only the English letters; every other character stays put.
#
#   Example: "ab-cd" -> "dc-ba"     "a-bC-dEf-ghIj" -> "j-Ih-gfE-dCba"
#
# Today's angle - stacks revisit:
#   A stack reverses things for free. Push every letter. Then walk the
#   string again: at a letter position, pop (you get the letters in
#   reverse); at any other position, copy the character.
#   O(n) time but O(n) extra space for the stack.
#   The two-pointer swap (Day 8 / Day 18) does the same with O(1) extra
#   space - both are below so you can compare.
# ============================================================


def is_letter(ch):
    code = ord(ch)
    return (65 <= code <= 90) or (97 <= code <= 122)


def reverse_only_letters_brute(s):
    # Brute force: the k-th letter from the left takes the k-th letter
    # from the right, found by counting from the end every time. O(n^2).
    out = []
    k = 0                               # how many letters we've placed so far
    for ch in s:
        if not is_letter(ch):
            out.append(ch)
            continue
        seen = -1
        for j in range(len(s) - 1, -1, -1):
            if is_letter(s[j]):
                seen += 1
                if seen == k:
                    out.append(s[j])
                    break
        k += 1
    return "".join(out)


def reverse_only_letters_stack(s):
    stack = []
    for ch in s:
        if is_letter(ch):
            stack.append(ch)            # letters go in...
    out = []
    for ch in s:
        if is_letter(ch):
            out.append(stack.pop())     # ...and come out reversed
        else:
            out.append(ch)
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
    print(reverse_only_letters_stack("ab-cd"))            # dc-ba
    print(reverse_only_letters_stack("a-bC-dEf-ghIj"))    # j-Ih-gfE-dCba
    print(reverse_only_letters("Test1ng-Leet=code-Q!"))   # Qedo1ct-eeLg=ntse-T!
