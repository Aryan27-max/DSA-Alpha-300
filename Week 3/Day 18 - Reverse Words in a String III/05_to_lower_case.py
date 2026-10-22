# ============================================================
# Day 18 - VARIANT: To Lower Case  (LeetCode 709)
# ============================================================
# The question:
#   Return s with every uppercase letter changed to lowercase.
#
#   Example: "Hello" -> "hello"     "LOVELY" -> "lovely"
#
# The big idea (ASCII arithmetic):
#   .lower() would be a one-liner - the point today is to see how it
#   works underneath. In ASCII:
#     'A' = 65 ... 'Z' = 90
#     'a' = 97 ... 'z' = 122
#   Every uppercase letter is exactly 32 below its lowercase twin.
#   So: if 65 <= ord(ch) <= 90, add 32. Leave everything else alone.
#   (32 is also bit 5, so ord(ch) | 32 does the same thing for letters.)
# ============================================================


def to_lower_case_brute(s):
    # Brute force: look each uppercase letter up in a hand-written alphabet.
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    out = []
    for ch in s:
        replaced = ch
        for i in range(26):
            if upper[i] == ch:
                replaced = lower[i]
                break
        out.append(replaced)
    return "".join(out)


def to_lower_case(s):
    out = []
    for ch in s:
        code = ord(ch)
        if 65 <= code <= 90:            # 'A'..'Z'
            out.append(chr(code + 32))  # jump to the lowercase twin
        else:
            out.append(ch)
    return "".join(out)


if __name__ == "__main__":
    print(to_lower_case("Hello"))         # hello
    print(to_lower_case("here"))          # here
    print(to_lower_case("LOVELY"))        # lovely
    print(to_lower_case_brute("aBc-D1"))  # abc-d1
