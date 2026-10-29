# ============================================================
# Day 23 - PRIMARY: Baseball Game  (LeetCode 682)
# ============================================================
# The question:
#   You get a list of operations (strings). Keep a record of scores:
#     an integer x -> record a new score x
#     "+"          -> record the sum of the previous two scores
#     "D"          -> record double the previous score
#     "C"          -> cancel (remove) the previous score
#   Return the sum of all scores left in the record.
#
#   Example: ["5","2","C","D","+"] -> 30
#            record: [5] -> [5,2] -> [5] -> [5,10] -> [5,10,15]  sum = 30
#
# The big idea (stack as running state):
#   The record only ever changes at its END -> it's a stack.
#   Every op only looks at the top one or two scores.
#   Keep a running total as you go: add when you push, subtract when you
#   pop. Then the answer is ready at the end without re-adding anything.
#   (No deque, and no sum(stack) inside the loop.)
# ============================================================


def cal_points_brute(operations):
    # Brute force: after every op, re-add the whole record from scratch.
    # (That's what calling sum(stack) inside the loop secretly does - O(n^2).)
    stack = []
    total = 0
    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
        total = 0
        for x in stack:                 # re-adding every single time
            total += x
    return total


def cal_points(operations):
    stack = []
    total = 0                           # always equals the sum of the stack

    for op in operations:
        if op == "+":
            score = stack[-1] + stack[-2]
            stack.append(score)
            total += score
        elif op == "D":
            score = 2 * stack[-1]
            stack.append(score)
            total += score
        elif op == "C":
            total -= stack.pop()        # cancelled score leaves the total too
        else:
            score = int(op)
            stack.append(score)
            total += score

    return total


if __name__ == "__main__":
    print(cal_points(["5", "2", "C", "D", "+"]))                      # 30
    print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))      # 27
    print(cal_points(["1", "C"]))                                     # 0
    print(cal_points_brute(["5", "2", "C", "D", "+"]))                # 30
