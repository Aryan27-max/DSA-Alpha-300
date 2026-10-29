# ============================================================
# Day 31 - VARIANT: Remove All Adjacent Duplicates In String  (LeetCode 1047)
# ============================================================
# The question:
#   Keep removing two equal neighbouring letters until none are left.
#
#   Example: "abbaca" -> "ca"      "azxxzy" -> "ay"
#
# Today's angle - the stack lives INSIDE the array (Day 23 used a list):
#   Combine Day 30's read/write pointers with a stack:
#   chars[0 .. write-1] IS the stack, and 'write' is its size.
#     copy chars[read] to chars[write]
#     if it equals chars[write - 1] -> they cancel: write -= 1 (pop both)
#     else                          -> write += 1 (push)
#   No separate stack list - just one char array and two pointers.
# ============================================================


def remove_duplicates_brute(s):
    chars = list(s)
    changed = True
    while changed:
        changed = False
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                chars.pop(i + 1)
                chars.pop(i)
                changed = True
                break
    return "".join(chars)


def remove_duplicates(s):
    chars = list(s)
    write = 0                           # size of the stack chars[0..write-1]

    for read in range(len(chars)):
        chars[write] = chars[read]      # tentatively push
        if write > 0 and chars[write - 1] == chars[write]:
            write -= 1                  # twins: pop the one underneath too
        else:
            write += 1                  # keep it

    return "".join(chars[:write])


if __name__ == "__main__":
    print(remove_duplicates("abbaca"))         # ca
    print(remove_duplicates("azxxzy"))         # ay
    print(remove_duplicates("aaaa"))           # (empty)
    print(remove_duplicates_brute("abbaca"))   # ca
