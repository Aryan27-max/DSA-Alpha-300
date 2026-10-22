# ============================================================
# Day 17 - PRIMARY: Longest Common Prefix  (LeetCode 14)
# ============================================================
# The question:
#   Return the longest prefix that EVERY string in the list starts with.
#   If there is none, return "".
#
#   Example: ["flower","flow","flight"] -> "fl"
#            ["dog","racecar","car"]    -> ""
#
# Two ways to scan:
#   Horizontal scan: start with the first word as the prefix, then trim it
#     down against each next word until it matches.
#   Vertical scan (column-wise): look at column 0 of every word, then
#     column 1, and so on. The first column where a word is too short or a
#     letter differs, stop. Everything before that column is the answer.
#   Vertical is usually better: it stops at the first mismatch and never
#   reads past the shortest prefix. (No os.path.commonprefix, takewhile,
#   or zip(*strs) tricks - walk by index.)
# ============================================================


def longest_common_prefix_horizontal(strs):
    # Horizontal scan: shrink the prefix word by word.
    if len(strs) == 0:
        return ""
    prefix_len = len(strs[0])
    for w in strs[1:]:
        i = 0
        while i < prefix_len and i < len(w) and w[i] == strs[0][i]:
            i += 1
        prefix_len = i                  # the prefix can only shrink
        if prefix_len == 0:
            return ""
    return strs[0][:prefix_len]


def longest_common_prefix(strs):
    # Vertical scan: check one column at a time across all words.
    if len(strs) == 0:
        return ""

    first = strs[0]
    for col in range(len(first)):
        ch = first[col]
        for w in strs[1:]:
            if col >= len(w) or w[col] != ch:
                return first[:col]      # mismatch (or a word ran out) -> stop here
    return first                        # the whole first word is common


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))   # fl
    print(longest_common_prefix(["dog", "racecar", "car"]))      # (empty)
    print(longest_common_prefix(["ab", "a"]))                    # a
    print(longest_common_prefix_horizontal(["interspecies", "interstellar", "interstate"]))  # inters
