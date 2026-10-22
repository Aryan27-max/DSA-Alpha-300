# ============================================================
# Day 19 - VARIANT: Find and Replace Pattern  (LeetCode 890)
# ============================================================
# The question:
#   Return every word in words that matches pattern, where "matches"
#   means there's a one-to-one letter mapping (same as isomorphic).
#
#   Example: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
#            -> ["mee","aqq"]
#
# Two approaches:
#   A) Run the two-dict isomorphic check on every word.
#   B) Normalize: replace each letter with "the order it first appeared".
#      "abb" -> (0,1,1), "mee" -> (0,1,1), "dkd" -> (0,1,0).
#      Two strings are isomorphic exactly when their normal forms match.
#      Compute the pattern's form once, then compare.
# ============================================================


def matches(word, pattern):
    # Two-dict bijection check from today's primary.
    if len(word) != len(pattern):
        return False
    w_to_p, p_to_w = {}, {}
    for i in range(len(word)):
        a, b = word[i], pattern[i]
        if a in w_to_p and w_to_p[a] != b:
            return False
        if b in p_to_w and p_to_w[b] != a:
            return False
        w_to_p[a] = b
        p_to_w[b] = a
    return True


def find_and_replace_pattern_two_dicts(words, pattern):
    result = []
    for w in words:
        if matches(w, pattern):
            result.append(w)
    return result


def normal_form(word):
    first_seen = {}                     # letter -> the order it first showed up
    form = []
    for ch in word:
        if ch not in first_seen:
            first_seen[ch] = len(first_seen)
        form.append(first_seen[ch])
    return form


def find_and_replace_pattern(words, pattern):
    target = normal_form(pattern)
    result = []
    for w in words:
        if normal_form(w) == target:
            result.append(w)
    return result


if __name__ == "__main__":
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    print(find_and_replace_pattern(words, "abb"))             # ['mee', 'aqq']
    print(find_and_replace_pattern_two_dicts(words, "abb"))   # ['mee', 'aqq']
    print(find_and_replace_pattern(["a", "b", "c"], "a"))     # ['a', 'b', 'c']
