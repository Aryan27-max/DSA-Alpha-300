# Day 27 · Implement Queue using Stacks
**Topic:** Two-stack FIFO simulation

Prove you can get FIFO out of LIFO: a stack reverses order, so two stacks reverse it back. Pour from the input stack to the output stack **only when the output is empty**, and every element moves at most once — that's the amortized O(1) argument. The variants go the other way (stack from queues), then build fixed-size rings, and finally use stacks of tweets in a small system design.

> No `deque`. It already *is* a queue and would trivialise the whole exercise. Two lists only.

---

## 1. Implement Queue using Stacks (PRIMARY) — `01_queue_using_stacks.py`

**Brute force:** One stack, rebuilt on every push so the oldest stays on top.
Time **O(n)** push, **O(1)** pop/peek · Space **O(n)**

**Optimal:** `in_stack` for pushes, `out_stack` for pops; pour only when `out_stack` is empty.
Time **amortized O(1)** per op (each element: pushed once, moved once, popped once) · Space **O(n)**

**Equivalent questions:** LeetCode 232 – [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) · GFG – "Queue using two Stacks"

---

## 2. Implement Stack using Queues — `02_stack_using_queues.py`
(The queue itself is hand-built: list + head pointer, queue operations only.)

**Brute force:** Two queues; `pop` moves n−1 items across.
Time **O(1)** push, **O(n)** pop · Space **O(n)**

**One queue:** After each push, rotate the queue n−1 times so the newest is at the front.
Time **O(n)** push, **O(1)** pop/top · Space **O(n)**

**Equivalent questions:** LeetCode 225 – [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) · GFG – "Stack using two queues"

---

## 3. Design Circular Queue — `03_design_circular_queue.py`

**Brute force:** Plain list with `pop(0)`.
Time **O(n)** deQueue · Space **O(k)**

**Optimal:** Fixed ring of k slots with `head` and `count`; positions wrap with `% k`.
Time **O(1)** every op · Space **O(k)**

**Equivalent questions:** LeetCode 622 – [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) · GFG – "Circular Queue | Set 1 (Introduction and Array Implementation)"

---

## 4. Design Circular Deque — `04_design_circular_deque.py`

**Brute force:** Plain list with `insert(0, …)` / `pop(0)`.
Time **O(n)** front ops · Space **O(k)**

**Optimal:** Same ring; `insertFront` steps `head` back with `(head − 1 + k) % k`; `deleteLast` just decrements `count`.
Time **O(1)** every op · Space **O(k)**

**Equivalent questions:** LeetCode 641 – [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) · GFG – "Implementation of Deque using circular array"

---

## 5. Moving Average from Data Stream — `05_moving_average_data_stream.py`
(Day 14: circular buffer · **Day 27: two-stack queue** · Day 28: `pop(0)` vs ring.)

**Brute force:** Re-add the last `size` values every call.
Time **O(size)** per call · Space **O(n)**

**Optimal here:** Running sum + today's two-stack queue; pop the oldest when the window is too big.
Time **amortized O(1)** per call · Space **O(size)**

**Equivalent questions:** LeetCode 346 – [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) (Premium) · LeetCode 933 – [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) (free, same queue window)

---

## 6. Design Twitter — `06_design_twitter.py`

**Brute force feed:** Gather every relevant tweet, insertion-sort by time, take 10.
Time **O(T²)** per feed (T = relevant tweets) · Space **O(T)**

**Optimal (no heap yet):** Each user's tweets are a stack (newest on top). Merge the tops: 10 times, pick the newest top among followed users and move that pointer down.
Time **O(1)** post/follow/unfollow, **O(10 · F)** feed (F = followees) · Space **O(users + tweets)**
*(With a heap the feed becomes O(F + 10 log F) — December.)*

**Equivalent questions:** LeetCode 355 – [Design Twitter](https://leetcode.com/problems/design-twitter/) · LeetCode 23 – [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (same k-way merge idea)
