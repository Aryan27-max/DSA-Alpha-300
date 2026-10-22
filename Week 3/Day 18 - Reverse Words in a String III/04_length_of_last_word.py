# ============================================================
# Day 18 - VARIANT: Length of Last Word  (LeetCode 58)
# ============================================================
# The question:
#   s has words and spaces (maybe trailing spaces too). Return the
#   length of the LAST word.
#
#   Example: "Hello World" -> 5     "   fly me   to   the moon  " -> 4
#
# The big idea (walk from the end):
#   No need to read the whole string or split it.
#   Start at the last character:
#     1. skip trailing spaces
#     2. count letters until you hit a space or the start
# ============================================================


def length_of_last_word_brute(s):
    # Brute force: split into words and measure the last one.
    words = s.split()
    return len(words[-1]) if words else 0


def length_of_last_word(s):
    i = len(s) - 1

    while i >= 0 and s[i] == " ":
        i -= 1                      # skip trailing spaces

    length = 0
    while i >= 0 and s[i] != " ":
        length += 1                 # count the last word's letters
        i -= 1

    return length


if __name__ == "__main__":
    print(length_of_last_word("Hello World"))                    # 5
    print(length_of_last_word("   fly me   to   the moon  "))    # 4
    print(length_of_last_word("luffy is still joyboy"))          # 6
