# ============================================================
# Day 26 - VARIANT: Largest Rectangle in Histogram  (LeetCode 84 - Hard)
# ============================================================
# The question:
#   heights[i] is the height of a bar of width 1. Find the area of the
#   biggest rectangle that fits inside the histogram.
#
#   Example: [2,1,5,6,2,3] -> 10   (bars 5 and 6, height 5, width 2)
#
# The big idea (monotonic INCREASING stack):
#   The best rectangle using bar i at full height stretches left and right
#   until it hits a SHORTER bar on each side.
#   Keep a stack of indexes with heights going UP.
#   When a shorter bar arrives at index i, every taller bar on top has
#   just found its right wall (i). Pop it:
#     height = its height
#     left wall = the index now on top of the stack (or -1 if empty)
#     width = i - left_wall - 1
#   Add a height-0 bar at the very end so everything gets popped.
# ============================================================


def largest_rectangle_brute(heights):
    # Brute force: every start, extend right while tracking the lowest bar.
    best = 0
    n = len(heights)
    for i in range(n):
        lowest = heights[i]
        for j in range(i, n):
            if heights[j] < lowest:
                lowest = heights[j]
            area = lowest * (j - i + 1)
            if area > best:
                best = area
    return best


def largest_rectangle_area(heights):
    stack = []                          # indexes, heights increasing upward
    best = 0
    n = len(heights)

    for i in range(n + 1):
        h = heights[i] if i < n else 0  # the fake 0 bar flushes the stack
        while len(stack) > 0 and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left_wall = stack[-1] if len(stack) > 0 else -1
            width = i - left_wall - 1
            if height * width > best:
                best = height * width
        stack.append(i)

    return best


if __name__ == "__main__":
    print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))   # 10
    print(largest_rectangle_area([2, 4]))               # 4
    print(largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]))  # 12
