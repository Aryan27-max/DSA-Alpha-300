# Intersection of 3 Sorted Arrays
#
# This one is different from the hashmap problems.
# Since all three arrays are already sorted, we can use three pointers.
#
# If all three values are equal, we found a common value.
# Otherwise, move the pointer with the smallest value.


def intersect_three(a, b, c):
    i = 0
    j = 0
    k = 0

    answer = []

    while i < len(a) and j < len(b) and k < len(c):

        if a[i] == b[j] and b[j] == c[k]:
            answer.append(a[i])
            i += 1
            j += 1
            k += 1

        else:
            smallest = min(a[i], b[j], c[k])

            if a[i] == smallest:
                i += 1

            if b[j] == smallest:
                j += 1

            if c[k] == smallest:
                k += 1

    return answer


a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]

print("Intersection:", intersect_three(a, b, c))
