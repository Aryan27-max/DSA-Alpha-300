# Find Common Characters
#
# A character should appear in the answer as many times as the
# minimum number of times it appears in every word.
#
# Example:
# ["bella", "label", "roller"]
# gives ["e", "l", "l"].
#
# We use a simple list of 26 counts instead of Counter.


def common_chars(words):
    # Start with a large value because we are going to take minimums.
    common = [float("inf")] * 26

    for word in words:
        freq = [0] * 26

        # Count characters in this word.
        for ch in word:
            freq[ord(ch) - ord("a")] += 1

        # Keep the smallest frequency seen so far.
        for i in range(26):
            common[i] = min(common[i], freq[i])

    answer = []

    # Add every common character the required number of times.
    for i in range(26):
        while common[i] > 0:
            answer.append(chr(i + ord("a")))
            common[i] -= 1

    return answer


words = ["bella", "label", "roller"]

print("Common characters:", common_chars(words))
