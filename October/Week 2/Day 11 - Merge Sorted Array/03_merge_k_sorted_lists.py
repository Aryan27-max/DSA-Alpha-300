# ============================================================
# Day 11 - VARIANT: Merge k Sorted Lists  (LeetCode 23 - Hard)
# ============================================================
# The question:
#   You get k sorted linked lists. Merge them all into one sorted list.
#
#   Example: [1->4->5, 1->3->4, 2->6] -> 1->1->2->3->4->4->5->6
#
# The big idea (divide and conquer - no heap yet):
#   The usual answer uses a min-heap, but heapq is banned until December.
#   Instead, merge the lists in PAIRS, like a tournament:
#     round 1: (list0 + list1), (list2 + list3), ...
#     round 2: merge those results in pairs again...
#   There are log k rounds and each round touches all N nodes once,
#   so it's O(N log k) - the same as the heap solution.
# ============================================================


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_pylist(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def merge_two(l1, l2):
    # Merge Two Sorted Lists from the previous file.
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1; l1 = l1.next
        else:
            tail.next = l2; l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next


def merge_k_lists_brute(lists):
    # Brute force: merge one list at a time into a growing result.
    # The result gets longer each time, so it's O(N * k).
    result = None
    for head in lists:
        result = merge_two(result, head)
    return result


def merge_k_lists(lists):
    if len(lists) == 0:
        return None

    while len(lists) > 1:
        next_round = []
        for i in range(0, len(lists), 2):
            first = lists[i]
            second = lists[i + 1] if i + 1 < len(lists) else None   # odd one out gets a bye
            next_round.append(merge_two(first, second))
        lists = next_round              # half as many lists now

    return lists[0]


if __name__ == "__main__":
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    print(to_pylist(merge_k_lists(lists)))          # [1, 1, 2, 3, 4, 4, 5, 6]
    print(to_pylist(merge_k_lists([])))             # []
    lists = [build_list([2]), build_list([]), build_list([-1])]
    print(to_pylist(merge_k_lists_brute(lists)))    # [-1, 2]
