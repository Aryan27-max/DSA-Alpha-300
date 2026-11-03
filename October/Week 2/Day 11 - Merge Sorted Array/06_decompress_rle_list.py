# ============================================================
# Day 11 - VARIANT: Decompress Run-Length Encoded List  (LeetCode 1313)
# ============================================================
# The question:
#   nums is a run-length encoding: pairs [freq, val, freq, val, ...].
#   Each pair means "val repeated freq times". Return the decompressed list.
#
#   Example: [1,2,3,4] -> [2,4,4,4]   (one 2, then three 4s)
#
# The big idea:
#   Walk two at a time. A read pointer jumps by 2; for each pair, append
#   val freq times. (Skip the list-multiply-and-extend shortcut and write
#   the loop - it keeps the read/write idea visible.)
# ============================================================


def decompress_brute(nums):
    # Build with list concatenation each time (creates a new list every pair).
    result = []
    for i in range(0, len(nums), 2):
        result = result + [nums[i + 1]] * nums[i]
    return result


def decompress_rle_list(nums):
    result = []
    for i in range(0, len(nums), 2):
        freq = nums[i]
        val = nums[i + 1]
        for _ in range(freq):
            result.append(val)      # write val, freq times
    return result


if __name__ == "__main__":
    print(decompress_rle_list([1, 2, 3, 4]))   # [2, 4, 4, 4]
    print(decompress_rle_list([1, 1, 2, 3]))   # [1, 3, 3]
