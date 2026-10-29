# ============================================================
# Day 26 - VARIANT: Daily Temperatures  (LeetCode 739)
# ============================================================
# The question:
#   For each day, how many days do you have to wait for a WARMER day?
#   0 if it never gets warmer.
#
#   Example: [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]
#
# The big idea (wait-days version of Next Greater Element):
#   Same monotonic decreasing stack, but store INDEXES - the answer is a
#   distance (warmer_day - waiting_day), not a value.
# ============================================================


def daily_temperatures_brute(temperatures):
    n = len(temperatures)
    result = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                break
    return result


def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []                              # indexes of days still waiting

    for today in range(len(temperatures)):
        while len(stack) > 0 and temperatures[stack[-1]] < temperatures[today]:
            day = stack.pop()
            result[day] = today - day       # how long that day waited
        stack.append(today)

    return result


if __name__ == "__main__":
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))   # [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures([30, 40, 50, 60]))                   # [1, 1, 1, 0]
    print(daily_temperatures([30, 60, 90]))                       # [1, 1, 0]
