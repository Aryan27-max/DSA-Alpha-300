# ============================================================
# Day 21 - VARIANT: Range Sum Query 2D - Immutable  (LeetCode 304)
# ============================================================
# The question:
#   Same as the primary, but for a 2D grid. sumRegion(r1, c1, r2, c2)
#   returns the sum of the rectangle with top-left (r1, c1) and
#   bottom-right (r2, c2), inclusive. Each query must be O(1).
#
#   Example: matrix = [[3,0,1,4,2],
#                      [5,6,3,2,1],
#                      [1,2,0,1,5],
#                      [4,1,0,1,7],
#                      [1,0,3,0,5]]
#            sumRegion(2,1,4,3) -> 8
#
# The big idea (2D prefix sum + inclusion-exclusion):
#   P[i][j] = sum of the rectangle from (0,0) to (i-1, j-1).
#   Build:  P[i+1][j+1] = matrix[i][j] + P[i][j+1] + P[i+1][j] - P[i][j]
#           (add top and left, but the top-left corner got added twice)
#   Query:  P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
#           (take the big box, cut off the strip above and the strip to
#            the left; the corner was cut twice, so add it back once)
# ============================================================


class NumMatrixBrute:
    def __init__(self, matrix):
        self.m = matrix

    def sumRegion(self, r1, c1, r2, c2):
        total = 0
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                total += self.m[r][c]
        return total


class NumMatrix:
    def __init__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        self.P = []
        for _ in range(rows + 1):
            self.P.append([0] * (cols + 1))     # extra row and column of zeros

        for i in range(rows):
            for j in range(cols):
                self.P[i + 1][j + 1] = (matrix[i][j]
                                        + self.P[i][j + 1]     # everything above
                                        + self.P[i + 1][j]     # everything to the left
                                        - self.P[i][j])        # corner counted twice

    def sumRegion(self, r1, c1, r2, c2):
        P = self.P
        return P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]


if __name__ == "__main__":
    grid = [[3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]]
    nm = NumMatrix(grid)
    print(nm.sumRegion(2, 1, 4, 3))   # 8
    print(nm.sumRegion(1, 1, 2, 2))   # 11
    print(nm.sumRegion(1, 2, 2, 4))   # 12
