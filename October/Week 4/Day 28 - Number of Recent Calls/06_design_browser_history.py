# ============================================================
# Day 28 - VARIANT: Design Browser History  (LeetCode 1472)
# ============================================================
# The question:
#   BrowserHistory(homepage):
#     visit(url)     - go to url; this erases all "forward" history
#     back(steps)    - go back up to `steps` pages, return the current url
#     forward(steps) - go forward up to `steps` pages, return the current url
#
#   Example: home "leetcode.com", visit google, facebook, youtube
#            back(1) -> facebook, back(1) -> google, forward(1) -> facebook
#            visit linkedin, forward(2) -> linkedin, back(2) -> google,
#            back(7) -> leetcode.com
#
# The big idea (in/out event tracking):
#   Version A - two stacks: back_stack (top = current page) and
#     forward_stack. back moves pages from back to forward; forward moves
#     them back; visit clears forward_stack. Each step is O(1), so
#     back/forward cost O(steps).
#   Version B - one list + two pointers:
#     cur  = index of the current page
#     last = index of the last page you could go forward to
#     visit overwrites history[cur + 1] and sets last = cur. The old
#     forward pages are still in the list but 'last' hides them - no need
#     to delete anything. back/forward are just pointer moves: O(1).
# ============================================================


class BrowserHistoryBrute:
    # Brute force: slice off the forward history on every visit (O(n) copy).
    def __init__(self, homepage):
        self.history = [homepage]
        self.cur = 0

    def visit(self, url):
        self.history = self.history[:self.cur + 1]
        self.history.append(url)
        self.cur += 1

    def back(self, steps):
        self.cur = self.cur - steps if self.cur - steps > 0 else 0
        return self.history[self.cur]

    def forward(self, steps):
        last = len(self.history) - 1
        self.cur = self.cur + steps if self.cur + steps < last else last
        return self.history[self.cur]


class BrowserHistoryStacks:
    def __init__(self, homepage):
        self.back_stack = [homepage]    # top is the current page
        self.forward_stack = []

    def visit(self, url):
        self.back_stack.append(url)
        self.forward_stack = []         # new visit wipes the forward history

    def back(self, steps):
        while steps > 0 and len(self.back_stack) > 1:
            self.forward_stack.append(self.back_stack.pop())
            steps -= 1
        return self.back_stack[-1]

    def forward(self, steps):
        while steps > 0 and len(self.forward_stack) > 0:
            self.back_stack.append(self.forward_stack.pop())
            steps -= 1
        return self.back_stack[-1]


class BrowserHistory:
    def __init__(self, homepage):
        self.history = [homepage]
        self.cur = 0
        self.last = 0

    def visit(self, url):
        self.cur += 1
        if self.cur == len(self.history):
            self.history.append(url)
        else:
            self.history[self.cur] = url   # overwrite instead of deleting
        self.last = self.cur               # forward pages beyond here are now invalid

    def back(self, steps):
        self.cur = self.cur - steps if self.cur - steps > 0 else 0
        return self.history[self.cur]

    def forward(self, steps):
        self.cur = self.cur + steps if self.cur + steps < self.last else self.last
        return self.history[self.cur]


if __name__ == "__main__":
    for cls in (BrowserHistoryStacks, BrowserHistory):
        b = cls("leetcode.com")
        b.visit("google.com"); b.visit("facebook.com"); b.visit("youtube.com")
        out = [b.back(1), b.back(1), b.forward(1)]
        b.visit("linkedin.com")
        out += [b.forward(2), b.back(2), b.back(7)]
        print(cls.__name__, out)
        # ['facebook.com', 'google.com', 'facebook.com', 'linkedin.com', 'google.com', 'leetcode.com']
