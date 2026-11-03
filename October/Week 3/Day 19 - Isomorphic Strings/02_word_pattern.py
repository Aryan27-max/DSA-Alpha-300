# ============================================================
# Day 19 - VARIANT: Word Pattern  (LeetCode 290)
# ============================================================
# The question:
#   pattern is letters, s is words separated by single spaces.
#   Return True if s follows the pattern with a one-to-one mapping
#   between letters and words.
#
#   Example: pattern = "abba", s = "dog cat cat dog" -> True
#            pattern = "abba", s = "dog cat cat fish" -> False
#            pattern = "abba", s = "dog dog dog dog" -> False  (a and b both -> dog)
#
# The big idea:
#   Exactly Isomorphic Strings, but the second side is WORDS instead of
#   characters. Split s (str .split() is allowed), check the counts
#   match, then use two dicts: letter->word and word->letter.
# ============================================================


def word_pattern_brute(pattern, s):
    # Brute force: compare every pair of positions.
    words = s.split()
    n = len(pattern)
    if n != len(words):
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if (pattern[i] == pattern[j]) != (words[i] == words[j]):
                return False
    return True


def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    letter_to_word = {}
    word_to_letter = {}

    for i in range(len(pattern)):
        p, w = pattern[i], words[i]
        if p in letter_to_word and letter_to_word[p] != w:
            return False
        if w in word_to_letter and word_to_letter[w] != p:
            return False
        letter_to_word[p] = w
        word_to_letter[w] = p

    return True


if __name__ == "__main__":
    print(word_pattern("abba", "dog cat cat dog"))    # True
    print(word_pattern("abba", "dog cat cat fish"))   # False
    print(word_pattern("aaaa", "dog cat cat dog"))    # False
    print(word_pattern("abba", "dog dog dog dog"))    # False
