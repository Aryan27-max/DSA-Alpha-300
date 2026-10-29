# Day 28 · Number of Recent Calls
**Topic:** Monotonic queue (sliding window of time)

When events arrive in time order, the oldest ones always leave from the **front** and new ones join at the **back** — a queue sliding over time. That's the exact shape of a rate limiter. Today you build it three ways and compare: `pop(0)` (simple but secretly O(n)), a head pointer (fast but memory grows), and a fixed circular buffer (fast *and* bounded).

> No `deque` or `bisect`. Start with a plain list and `pop(0)`, then optimise to a ring buffer and compare.

---

## 1. Number of Recent Calls (PRIMARY) — `01_number_of_recent_calls.py`

**v1 – list + `pop(0)`:** Each `pop(0)` shifts every element.
Time **O(n)** per ping worst case · Space **O(window)**

**v2 – list + head pointer:** Move `head` instead of deleting.
Time **amortized O(1)** · Space **O(total pings)** — the list never shrinks

**v3 – circular buffer (optimal):** 3001 fixed slots (times are distinct, so at most 3001 fit in a 3001 ms window).
Time **amortized O(1)** · Space **O(3001) = O(1)**

**Equivalent questions:** LeetCode 933 – [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)

---

## 2. Design Hit Counter — `02_design_hit_counter.py`

**Brute force:** Keep all hits forever, count the window each time.
Time **O(total hits)** per `getHits` · Space **O(total hits)**

**Queue version:** Drop old timestamps from the front.
Time **amortized O(1)** · Space **O(hits in the last 300 s)**

**Optimal (bounded memory):** 300 ring buckets of `(second, count)`; reset a bucket when it holds an old second.
Time **O(1)** hit, **O(300)** getHits · Space **O(300)** no matter how many hits

**Equivalent questions:** LeetCode 362 – [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) (Premium) · LeetCode 933 – [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) (free)

---

## 3. Logger Rate Limiter — `03_logger_rate_limiter.py`

**Brute force:** Keep every printed message; scan for one in the last 10 s.
Time **O(n)** per call · Space **O(n)**

**Dict version:** `message → next allowed time`.
Time **O(1)** · Space **O(all messages ever)**

**Bounded version:** Queue of `(time, message)` from the last 10 s + a set of those messages.
Time **amortized O(1)** · Space **O(messages in the last 10 s)**

**Equivalent questions:** LeetCode 359 – [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) (Premium) · LeetCode 933 (free, same window idea)

---

## 4. Sliding Window Maximum — `04_sliding_window_maximum.py`
(Day 25: two max-stacks · Day 26: list + head deque · **Day 28: k-slot ring deque**.)

**Brute force:** Scan each window.
Time **O(n·k)** · Space **O(1)** extra

**Optimal:** Monotonic deque stored in a ring of exactly k slots.
Time **O(n)** · Space **O(k)**

**Equivalent questions:** LeetCode 239 – [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) · GFG – "Maximum of all subarrays of size k"

---

## 5. Moving Average from Data Stream — `05_moving_average_data_stream.py`
(Day 14 ring + head · Day 27 two-stack queue · **Day 28 `pop(0)` vs ring side by side**.)

**`pop(0)` version:** Looks O(1), really **O(size)** per call · Space **O(size)**

**Ring buffer:** The slot being overwritten is the value leaving.
Time **O(1)** per call · Space **O(size)**

**Equivalent questions:** LeetCode 346 – [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) (Premium) · LeetCode 643 – [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) (free)

---

## 6. Design Browser History — `06_design_browser_history.py`

**Brute force:** Slice off forward history on every visit.
Time **O(n)** visit · Space **O(n)**

**Two stacks:** back stack + forward stack.
Time **O(1)** visit, **O(steps)** back/forward · Space **O(n)**

**Optimal:** One list + `cur` + `last`; visit overwrites and moves `last`, back/forward just move `cur`.
Time **O(1)** every op · Space **O(n)**

**Equivalent questions:** LeetCode 1472 – [Design Browser History](https://leetcode.com/problems/design-browser-history/)
