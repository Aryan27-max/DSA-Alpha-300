# ============================================================
# Day 7 - VARIANT: Find Common Characters  (LeetCode 1002)
# ============================================================
# The question:
#   Given a list of words, return every character that shows up in
#   ALL the words, including duplicates.
#
#   Example: ["bella", "label", "roller"] -> ["e", "l", "l"]
#
# The big idea (intersection across k lists):
#   For every letter, the answer can use it at most
#       min(count in word1, count in word2, ..., count in wordk) times.
#   Keep a 26-slot list of "best so far" counts and shrink it word by word.
# ============================================================


def common_chars_brute(words):
    # Brute force: take letters of the first word one by one,
    # and remove a matching copy from every other word if all have it.
    others = []
    for w in words[1:]:
        others.append(list(w))      # editable copies

    result = []
    for ch in words[0]:
        in_all = True
        for letters in others:
            if ch not in letters:
                in_all = False
                break
        if in_all:
            for letters in others:
                letters.remove(ch)  # use up one copy in each word
            result.append(ch)
    return result


def letter_counts(word):
    # Hand-made counter: slot 0 = 'a', slot 1 = 'b', ... slot 25 = 'z'
    counts = [0] * 26
    for ch in word:
        counts[ord(ch) - ord('a')] += 1
    return counts


def common_chars(words):
    common = letter_counts(words[0])        # start with the first word's counts

    for w in words[1:]:
        current = letter_counts(w)
        for i in range(26):
            if current[i] < common[i]:
                common[i] = current[i]      # can only keep as many as every word has

    result = []
    for i in range(26):
        for _ in range(common[i]):
            result.append(chr(ord('a') + i))
    return result


if __name__ == "__main__":
    print(common_chars(["bella", "label", "roller"]))   # ['e', 'l', 'l']
    print(common_chars(["cool", "lock", "cook"]))       # ['c', 'o']
