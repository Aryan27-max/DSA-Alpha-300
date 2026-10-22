# ============================================================
# Day 17 - VARIANT: Find Common Characters  (LeetCode 1002)
# ============================================================
# The question:
#   Return every character that shows up in ALL the words, including
#   duplicates (if 'l' is in every word twice, list it twice).
#
#   Example: ["bella","label","roller"] -> ["e","l","l"]
#
# The big idea (char overlap across lists):
#   Longest Common Prefix compares words position by position. Here
#   position doesn't matter - only counts. Think of it as a "vertical scan"
#   over the 26 letter columns: for each letter, the answer can use it
#   min(count in each word) times.
#   Keep a 26-slot "common" count and shrink it word by word.
# ============================================================


def common_chars_brute(words):
    # Brute force: for every letter of the first word, remove one copy from
    # each other word if all of them have it.
    others = [list(w) for w in words[1:]]
    result = []
    for ch in words[0]:
        if all_have(others, ch):
            for letters in others:
                letters.remove(ch)
            result.append(ch)
    return result


def all_have(lists, ch):
    for letters in lists:
        if ch not in letters:
            return False
    return True


def common_chars(words):
    common = [0] * 26
    for ch in words[0]:
        common[ord(ch) - 97] += 1

    for w in words[1:]:
        counts = [0] * 26
        for ch in w:
            counts[ord(ch) - 97] += 1
        for i in range(26):
            if counts[i] < common[i]:
                common[i] = counts[i]       # keep the smallest count seen so far

    result = []
    for i in range(26):
        for _ in range(common[i]):
            result.append(chr(97 + i))
    return result


if __name__ == "__main__":
    print(common_chars(["bella", "label", "roller"]))   # ['e', 'l', 'l']
    print(common_chars(["cool", "lock", "cook"]))       # ['c', 'o']
