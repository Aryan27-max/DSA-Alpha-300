# ============================================================
# Day 16 - VARIANT: Increasing Decreasing String  (LeetCode 1370)
# ============================================================
# The question:
#   Build the result by repeating until s is used up:
#     - go UP the alphabet: take the smallest letter left, then the next
#       bigger one, and so on (one of each).
#     - then go DOWN: take the biggest letter left, then the next smaller...
#   Return the result.
#
#   Example: "aaaabbbbcccc" -> "abccbaabccba"
#
# The big idea (frequency array + ordered scan):
#   Letters are a-z, so a 26-slot count list IS already "sorted".
#   Sweep index 0 -> 25 taking one of each available letter, then
#   25 -> 0, and repeat until we've placed every character.
# ============================================================


def sort_string_brute(s):
    # Brute force: keep a list of remaining chars and search it for each pick.
    remaining = list(s)
    result = []
    while remaining:
        last = ""
        while True:                                 # increasing step
            pick = None
            for ch in remaining:
                if ch > last and (pick is None or ch < pick):
                    pick = ch
            if pick is None:
                break
            result.append(pick)
            remaining.remove(pick)
            last = pick
        last = "{"                                  # '{' comes right after 'z'
        while True:                                 # decreasing step
            pick = None
            for ch in remaining:
                if ch < last and (pick is None or ch > pick):
                    pick = ch
            if pick is None:
                break
            result.append(pick)
            remaining.remove(pick)
            last = pick
    return "".join(result)


def sort_string(s):
    counts = [0] * 26
    for ch in s:
        counts[ord(ch) - 97] += 1

    result = []
    while len(result) < len(s):
        for i in range(26):                 # going up a -> z
            if counts[i] > 0:
                result.append(chr(97 + i))
                counts[i] -= 1
        for i in range(25, -1, -1):         # going down z -> a
            if counts[i] > 0:
                result.append(chr(97 + i))
                counts[i] -= 1

    return "".join(result)


if __name__ == "__main__":
    print(sort_string("aaaabbbbcccc"))         # abccbaabccba
    print(sort_string("rat"))                  # art
    print(sort_string_brute("aaaabbbbcccc"))   # abccbaabccba
