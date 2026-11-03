# ============================================================
# Day 19 - VARIANT: Groups of Special-Equivalent Strings  (LeetCode 893)
# ============================================================
# The question:
#   In one move you may swap two characters at EVEN indexes, or two
#   characters at ODD indexes. Two words are "special-equivalent" if
#   some moves turn one into the other. Return how many groups there are.
#
#   Example: ["abcd","cdab","cbad","xyzz","zzxy","zzyx"] -> 3
#            groups: [abcd, cdab, cbad], [xyzz, zzxy], [zzyx]
#
# The big idea (char equivalence groups -> a signature):
#   Even positions can be shuffled freely among themselves, same for odd.
#   So what never changes is: the letter COUNTS at even positions, and
#   the letter counts at odd positions.
#   Signature = (26 even counts) + (26 odd counts), as a tuple.
#   Same signature = same group. Count distinct signatures with a set.
# ============================================================


def signature(word):
    counts = [0] * 52                   # 0..25 for even positions, 26..51 for odd
    for i in range(len(word)):
        offset = 0 if i % 2 == 0 else 26
        counts[offset + ord(word[i]) - 97] += 1
    return tuple(counts)


def num_special_equiv_groups_brute(words):
    # Brute force: compare each word's signature with one word from every group so far.
    reps = []                           # one representative per group
    for w in words:
        found = False
        for r in reps:
            if signature(r) == signature(w):
                found = True
                break
        if not found:
            reps.append(w)
    return len(reps)


def num_special_equiv_groups(words):
    groups = set()
    for w in words:
        groups.add(signature(w))
    return len(groups)


if __name__ == "__main__":
    print(num_special_equiv_groups(["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]))  # 3
    print(num_special_equiv_groups(["abc", "acb", "bac", "bca", "cab", "cba"]))        # 3
