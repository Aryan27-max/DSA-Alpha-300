# ============================================================
# Day 31 - VARIANT: Simplify Path  (LeetCode 71)
# ============================================================
# The question:
#   Turn an absolute Unix path into its simplest form:
#     '.'  = current folder (ignore it)
#     '..' = go up one folder (ignore if already at the root)
#     multiple slashes '//' count as one
#     any other name (even '...') is a normal folder name
#   The result starts with '/', has single slashes, and no trailing '/'.
#
#   Example: "/home/"              -> "/home"
#            "/home//foo/"         -> "/home/foo"
#            "/home/user/Documents/../Pictures" -> "/home/user/Pictures"
#            "/../"                -> "/"
#
# The big idea (a stack of folder names):
#   Walking into a folder = push. '..' = pop (like backspace!).
#   Version 1 uses split('/') (a str primitive, allowed).
#   Version 2 tokenizes by walking the characters ourselves - no split.
# ============================================================


def simplify_path_split(path):
    stack = []
    for part in path.split("/"):
        if part == "" or part == ".":
            continue                    # empty piece (from //) or "stay here"
        if part == "..":
            if len(stack) > 0:
                stack.pop()             # go up one folder
        else:
            stack.append(part)          # go into a folder
    return "/" + "/".join(stack)


def simplify_path(path):
    stack = []
    i = 0
    n = len(path)

    while i < n:
        while i < n and path[i] == "/":
            i += 1                      # skip any run of slashes
        start = i
        while i < n and path[i] != "/":
            i += 1                      # read one name
        name = path[start:i]

        if name == "" or name == ".":
            continue
        if name == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(name)

    return "/" + "/".join(stack)


if __name__ == "__main__":
    print(simplify_path("/home/"))                             # /home
    print(simplify_path("/home//foo/"))                        # /home/foo
    print(simplify_path("/home/user/Documents/../Pictures"))   # /home/user/Pictures
    print(simplify_path("/../"))                               # /
    print(simplify_path("/.../a/../b/c/../d/./"))              # /.../b/d
