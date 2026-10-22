# ============================================================
# Day 18 - VARIANT: String Compression  (LeetCode 443)
# ============================================================
# The question:
#   chars is a list of characters. Compress it IN PLACE: each run of the
#   same character becomes the character, followed by the run length if
#   it's more than 1 (written as separate digit characters, e.g. "1","2").
#   Return the new length. Use O(1) extra space.
#
#   Example: ["a","a","b","b","c","c","c"] -> 6, ["a","2","b","2","c","3"]
#            ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#            -> 4, ["a","b","1","2"]
#
# The big idea (read pointer + write pointer, from Day 10):
#   read finds the end of each run. write puts down the character, then
#   the digits of the run length. The compressed form is never longer
#   than the original, so write never overtakes read.
#   We write the digits ourselves (peel with % 10, then flip them with
#   the Day 9 swap) instead of using str().
# ============================================================


def compress_brute(chars):
    # Brute force: build the answer in a new list, then copy it back. O(n) space.
    out = []
    i = 0
    while i < len(chars):
        j = i
        while j < len(chars) and chars[j] == chars[i]:
            j += 1
        out.append(chars[i])
        if j - i > 1:
            for d in str(j - i):
                out.append(d)
        i = j
    for k in range(len(out)):
        chars[k] = out[k]
    return len(out)


def compress(chars):
    write = 0
    read = 0
    n = len(chars)

    while read < n:
        ch = chars[read]
        run = 0
        while read < n and chars[read] == ch:
            read += 1
            run += 1                        # measure this run

        chars[write] = ch
        write += 1

        if run > 1:
            digit_start = write
            while run > 0:
                chars[write] = chr(ord('0') + run % 10)   # last digit first
                write += 1
                run //= 10
            # digits came out backwards ("21" for 12) -> flip them in place
            left, right = digit_start, write - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

    return write


if __name__ == "__main__":
    a = ["a", "a", "b", "b", "c", "c", "c"]
    k = compress(a)
    print(k, a[:k])     # 6 ['a', '2', 'b', '2', 'c', '3']

    b = ["a"]
    k = compress(b)
    print(k, b[:k])     # 1 ['a']

    c = ["a"] + ["b"] * 12
    k = compress(c)
    print(k, c[:k])     # 4 ['a', 'b', '1', '2']
