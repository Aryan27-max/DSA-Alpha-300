# ============================================================
# Day 11 - VARIANT: Merge Two Sorted Lists  (LeetCode 21)
# ============================================================
# The question:
#   Two sorted linked lists. Splice them together into one sorted list
#   (reuse the existing nodes) and return its head.
#
#   Example: 1->2->4  and  1->3->4  ->  1->1->2->3->4->4
#
# The big idea:
#   Use a dummy node as a fake start so we never special-case the head.
#   Keep a tail pointer. Each step, attach the smaller front node to the
#   tail and move forward in that list. When one list ends, attach the rest
#   of the other in one go.
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


def merge_two_lists_recursive(l1, l2):
    # Recursive version: the smaller head wins, the rest is a smaller problem.
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.val <= l2.val:
        l1.next = merge_two_lists_recursive(l1.next, l2)
        return l1
    l2.next = merge_two_lists_recursive(l1, l2.next)
    return l2


def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1          # attach the smaller node
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2    # whatever is left is already sorted
    return dummy.next


if __name__ == "__main__":
    print(to_pylist(merge_two_lists(build_list([1, 2, 4]), build_list([1, 3, 4]))))   # [1, 1, 2, 3, 4, 4]
    print(to_pylist(merge_two_lists(build_list([]), build_list([0]))))                 # [0]
    print(to_pylist(merge_two_lists_recursive(build_list([5]), build_list([1, 2]))))  # [1, 2, 5]
