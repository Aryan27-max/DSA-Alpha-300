# ============================================================
# Day 16 - VARIANT: Sort Characters By Frequency  (LeetCode 451)
# ============================================================
# The question:
#   Rearrange s so the most frequent characters come first. Each
#   character's copies stay together. Ties can be in any order.
#
#   Example: "tree" -> "eert" (or "eetr")
#            "Aabb" -> "bbAa" (or "bbaA")
#
# The big idea (bucket sort by count - no sorted()):
#   1. Count every character.
#   2. Make buckets 0..n. bucket[c] holds every character that appears
#      exactly c times. (No count can be bigger than n.)
#   3. Walk the buckets from n down to 1 and write each character c times.
#   That's O(n) - faster than sorting the counts.
# ============================================================


def frequency_sort_brute(s):
    # Brute force: repeatedly pick the character with the highest remaining count.
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    result = []
    while len(counts) > 0:
        best = None
        for ch in counts:
            if best is None or counts[ch] > counts[best]:
                best = ch
        for _ in range(counts[best]):
            result.append(best)
        del counts[best]
    return "".join(result)


def frequency_sort(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    buckets = []
    for _ in range(len(s) + 1):
        buckets.append([])              # one empty bucket per possible count
    for ch in counts:
        buckets[counts[ch]].append(ch)

    result = []
    for c in range(len(s), 0, -1):      # highest count first
        for ch in buckets[c]:
            for _ in range(c):
                result.append(ch)
    return "".join(result)


if __name__ == "__main__":
    print(frequency_sort("tree"))     # eert (or eetr)
    print(frequency_sort("cccaaa"))   # cccaaa (or aaaccc)
    print(frequency_sort("Aabb"))     # bbAa (or bbaA)
