# ============================================================
# Day 15 - VARIANT: Determine if Two Strings Are Close  (LeetCode 1657)
# ============================================================
# The question:
#   Two strings are "close" if you can turn one into the other using:
#     Op 1: swap any two characters (reorder freely).
#     Op 2: swap the roles of two EXISTING letters (every a becomes b and
#           every b becomes a).
#   Return True if word1 and word2 are close.
#
#   Example: "abc", "bca" -> True        "a", "aa" -> False
#            "cabbba", "abbccc" -> True
#
# The big idea (char-count equality, one level up):
#   Op 1 means order doesn't matter - only counts.
#   Op 2 means WHICH letter has which count doesn't matter either.
#   So the strings are close exactly when:
#     (a) they use the same SET of letters (op 2 can't invent new letters)
#     (b) the multiset of counts is the same, e.g. {1, 2, 3} for both.
#   For (b), count "how many letters have count c" in a dict for each
#   word and compare - no sorting needed.
# ============================================================


def counts_of(word):
    c = {}
    for ch in word:
        c[ch] = c.get(ch, 0) + 1
    return c


def close_strings_brute(word1, word2):
    # "Brute" version: sort both count lists with insertion sort and compare.
    if len(word1) != len(word2):
        return False
    c1, c2 = counts_of(word1), counts_of(word2)
    if len(c1) != len(c2):
        return False
    for ch in c1:
        if ch not in c2:
            return False

    def ins_sort(a):
        for i in range(1, len(a)):
            cur, j = a[i], i - 1
            while j >= 0 and a[j] > cur:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = cur
        return a

    f1 = ins_sort([c1[k] for k in c1])
    f2 = ins_sort([c2[k] for k in c2])
    return f1 == f2


def close_strings(word1, word2):
    if len(word1) != len(word2):
        return False

    c1 = counts_of(word1)
    c2 = counts_of(word2)

    # (a) same set of letters
    if len(c1) != len(c2):
        return False
    for ch in c1:
        if ch not in c2:
            return False

    # (b) same multiset of counts: "how many letters appear exactly c times?"
    freq1 = {}
    for ch in c1:
        freq1[c1[ch]] = freq1.get(c1[ch], 0) + 1
    freq2 = {}
    for ch in c2:
        freq2[c2[ch]] = freq2.get(c2[ch], 0) + 1

    if len(freq1) != len(freq2):
        return False
    for c in freq1:
        if freq2.get(c, 0) != freq1[c]:
            return False
    return True


if __name__ == "__main__":
    print(close_strings("abc", "bca"))          # True
    print(close_strings("a", "aa"))             # False
    print(close_strings("cabbba", "abbccc"))    # True
    print(close_strings("uau", "ssx"))          # False
