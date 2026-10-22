# ============================================================
# Day 19 - PRIMARY: Isomorphic Strings  (LeetCode 205)
# ============================================================
# The question:
#   s and t are isomorphic if you can replace characters in s to get t,
#   where:
#     - every copy of a character is replaced by the SAME character, and
#     - no two different characters are replaced by the same character.
#   (A character may map to itself.)
#
#   Example: "egg", "add"   -> True   (e->a, g->d)
#            "foo", "bar"   -> False  (o would need to be both a and r)
#            "badc", "baba" -> False  (b->b and d->b: two letters share 'b')
#
# The big idea (map BOTH directions):
#   One dict s->t catches "o can't be both a and r".
#   But it MISSES "b and d both turn into b" - each one maps consistently,
#   they just collide. That's the subtle bug: a one-way map isn't enough.
#   So keep a second dict t->s. Every pair (s[i], t[i]) must agree with
#   BOTH dicts. Together they make the mapping a bijection (one-to-one).
#   (No len(set(zip(s,t))) == len(set(s)) == len(set(t)) trick.)
# ============================================================


def is_isomorphic_one_way_BUGGY(s, t):
    # Only checks s -> t. Kept here on purpose to show why it's wrong.
    s_to_t = {}
    for i in range(len(s)):
        a, b = s[i], t[i]
        if a in s_to_t and s_to_t[a] != b:
            return False
        s_to_t[a] = b
    return True                     # "badc","baba" wrongly returns True


def is_isomorphic_brute(s, t):
    # Brute force: for every pair of positions, "same in s" must equal "same in t".
    n = len(s)
    if n != len(t):
        return False
    for i in range(n):
        for j in range(i + 1, n):
            if (s[i] == s[j]) != (t[i] == t[j]):
                return False
    return True


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}                     # what each s-char turns into
    t_to_s = {}                     # which s-char produced each t-char

    for i in range(len(s)):
        a, b = s[i], t[i]

        if a in s_to_t and s_to_t[a] != b:
            return False            # a already turns into something else
        if b in t_to_s and t_to_s[b] != a:
            return False            # b is already "taken" by a different letter

        s_to_t[a] = b
        t_to_s[b] = a

    return True


if __name__ == "__main__":
    print(is_isomorphic("egg", "add"))                  # True
    print(is_isomorphic("foo", "bar"))                  # False
    print(is_isomorphic("paper", "title"))              # True
    print(is_isomorphic("badc", "baba"))                # False
    print(is_isomorphic_one_way_BUGGY("badc", "baba"))  # True  <- the bug!
