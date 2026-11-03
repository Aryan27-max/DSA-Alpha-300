# ============================================================
# Day 8 - VARIANT: Palindrome Linked List  (LeetCode 234)
# ============================================================
# The question:
#   Given the head of a singly linked list, return True if the values
#   read the same forwards and backwards.
#   Follow-up: O(n) time and O(1) space.
#
#   Example: 1 -> 2 -> 2 -> 1 -> True      1 -> 2 -> False
#
# The big idea:
#   We can't walk backwards in a singly linked list. So:
#   1. Find the middle with slow/fast pointers (fast moves 2, slow moves 1).
#   2. Reverse the second half in place.
#   3. Walk the first half and the reversed second half together, comparing.
#   (Bonus: reverse the second half back so we don't damage the input.)
# ============================================================


class ListNode:
    # A tiny hand-made linked list node.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    # Helper: turn a Python list into a linked list, return the head.
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def is_palindrome_brute(head):
    # Brute force: copy values into a list, then two pointers. O(n) space.
    vals = []
    node = head
    while node:
        vals.append(node.val)
        node = node.next
    i, j = 0, len(vals) - 1
    while i < j:
        if vals[i] != vals[j]:
            return False
        i += 1
        j -= 1
    return True


def reverse(head):
    # Reverse a linked list in place, return the new head.
    prev = None
    curr = head
    while curr:
        nxt = curr.next     # save the rest of the list
        curr.next = prev    # point this node backwards
        prev = curr         # step forward
        curr = nxt
    return prev


def is_palindrome(head):
    if head is None or head.next is None:
        return True

    # 1. find the end of the first half
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # 2. reverse the second half
    second = reverse(slow.next)

    # 3. compare both halves
    p1, p2 = head, second
    result = True
    while p2:                       # second half is the same length or shorter
        if p1.val != p2.val:
            result = False
            break
        p1 = p1.next
        p2 = p2.next

    # 4. put the list back the way we found it
    slow.next = reverse(second)
    return result


if __name__ == "__main__":
    print(is_palindrome(build_list([1, 2, 2, 1])))      # True
    print(is_palindrome(build_list([1, 2])))            # False
    print(is_palindrome(build_list([1, 2, 3, 2, 1])))   # True
