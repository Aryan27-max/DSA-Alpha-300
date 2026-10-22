# ============================================================
# Day 17 - VARIANT: Check If a Word Occurs As a Prefix of Any Word in a Sentence
#                   (LeetCode 1455)
# ============================================================
# The question:
#   sentence is words separated by single spaces. Return the 1-based
#   position of the FIRST word that starts with searchWord, or -1.
#
#   Example: sentence = "i love eating burger", searchWord = "burg" -> 4
#            sentence = "this problem is an easy problem", searchWord = "pro" -> 2
#
# The big idea (prefix check between two words, char by char):
#   Walk the sentence once. At the start of each word, compare characters
#   with searchWord by index until either it fully matches or a mismatch
#   happens. No split needed - track word starts as you go.
# ============================================================


def is_prefix_of_word_brute(sentence, search_word):
    # Simple version: split into words, compare each word's first letters by index.
    words = sentence.split(" ")
    for idx in range(len(words)):
        w = words[idx]
        if len(w) >= len(search_word):
            ok = True
            for i in range(len(search_word)):
                if w[i] != search_word[i]:
                    ok = False
                    break
            if ok:
                return idx + 1
    return -1


def is_prefix_of_word(sentence, search_word):
    word_number = 1
    i = 0
    n = len(sentence)

    while i < n:
        # i is at the start of a word: try to match search_word here
        j = 0
        while j < len(search_word) and i + j < n and sentence[i + j] == search_word[j]:
            j += 1
        if j == len(search_word):
            return word_number          # matched every character of search_word

        # skip to the start of the next word
        while i < n and sentence[i] != " ":
            i += 1
        i += 1                          # jump over the space
        word_number += 1

    return -1


if __name__ == "__main__":
    print(is_prefix_of_word("i love eating burger", "burg"))                 # 4
    print(is_prefix_of_word("this problem is an easy problem", "pro"))       # 2
    print(is_prefix_of_word("i am tired", "you"))                            # -1
