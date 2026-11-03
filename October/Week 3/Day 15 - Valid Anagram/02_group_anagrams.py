# ============================================================
# Day 15 - VARIANT: Group Anagrams  (LeetCode 49)
# ============================================================
# The question:
#   Group together the words that are anagrams of each other.
#   Return the groups in any order.
#
#   Example: ["eat","tea","tan","ate","nat","bat"]
#            -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#
# The big idea (anagram signature):
#   Anagrams share the same letter counts. Turn each word into a
#   "signature" = a tuple of 26 counts (a tuple can be a dict key, a
#   list can't). Words with the same signature go in the same group.
#   Counting is O(L) per word - faster than sorting each word (O(L log L)),
#   and sorted() is banned anyway.
# ============================================================


def signature(word):
    counts = [0] * 26
    for ch in word:
        counts[ord(ch) - ord('a')] += 1
    return tuple(counts)                # tuples are hashable -> usable as a key


def group_anagrams_brute(strs):
    # Brute force: compare every word with the first word of each existing group.
    groups = []
    for w in strs:
        placed = False
        for g in groups:
            if signature(g[0]) == signature(w):
                g.append(w)
                placed = True
                break
        if not placed:
            groups.append([w])
    return groups


def group_anagrams(strs):
    groups = {}                         # signature -> list of words
    for w in strs:
        key = signature(w)
        if key not in groups:
            groups[key] = []
        groups[key].append(w)

    result = []
    for key in groups:
        result.append(groups[key])
    return result


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(group_anagrams([""]))        # [['']]
    print(group_anagrams(["a"]))       # [['a']]
