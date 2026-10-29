# ============================================================
# Day 31 - VARIANT: Decoded String at Index  (LeetCode 880)
# ============================================================
# The question:
#   s is an encoded string read left to right onto a "tape":
#     a letter   -> write it on the tape
#     a digit d  -> the whole tape so far is repeated d times in total
#   Return the k-th letter (1-indexed) of the final tape.
#   The tape can be astronomically long, so you can't build it.
#
#   Example: s = "leet2code3", k = 10 -> "o"
#            tape = "leetleetcodeleetleetcodeleetleetcode"
#            s = "ha22", k = 5 -> "h"     (tape "hahahaha")
#
# The big idea (decode run-length BACKWARDS):
#   Pass 1: compute only the LENGTH of the tape (size).
#   Pass 2: walk s from the END, "un-doing" each step:
#     k = k % size  - a repeated tape looks the same every 'size' letters,
#                     so we only care where k lands inside one copy
#     if k == 0 and this char is a letter -> it's the answer
#     if this char is a digit d -> size = size // d   (undo the repeat)
#     else (a letter)           -> size -= 1         (undo the write)
#   Same "read it backwards with a counter" move as today's primary.
# ============================================================


def decode_at_index_brute(s, k):
    # Brute force: actually build the tape (stop once it's long enough).
    tape = []
    for ch in s:
        if ch.isdigit():
            copy = tape[:]
            for _ in range(int(ch) - 1):
                tape.extend(copy)
                if len(tape) >= k:
                    break
        else:
            tape.append(ch)
        if len(tape) >= k:
            break
    return tape[k - 1]


def decode_at_index(s, k):
    size = 0
    for ch in s:                        # pass 1: how long is the tape?
        if ch.isdigit():
            size *= int(ch)
        else:
            size += 1

    for i in range(len(s) - 1, -1, -1): # pass 2: walk backwards
        ch = s[i]
        k %= size
        if k == 0 and not ch.isdigit():
            return ch
        if ch.isdigit():
            size //= int(ch)            # undo the repeat
        else:
            size -= 1                   # undo writing this letter

    return ""


if __name__ == "__main__":
    print(decode_at_index("leet2code3", 10))           # o
    print(decode_at_index("ha22", 5))                  # h
    print(decode_at_index("a2345678999999999999999", 1))  # a
    print(decode_at_index_brute("leet2code3", 10))     # o
