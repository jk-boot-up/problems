# 347. Top K Frequent Elements — v1: Counting + min-heap of size k

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem

Return the `k` most frequent elements of `nums`, in any order. The answer is guaranteed to be unique.

**Example**
```
nums = [1,1,1,2,2,3], k = 2 → [1,2]
nums = [1], k = 1            → [1]
```

**Constraints**
* `1 <= nums.length <= 10^5`; `1 <= k <=` number of distinct values

**Follow-up:** better than O(n log n).

## Approach: Counting + min-heap of size k

> Keep the k most frequent values in a min-heap ordered by count.

**Heap.** Count with `MyHashMap`, then push `(value, count)` into a min-heap by count, popping whenever it holds more than `k`.

* Time: **O(n log k)** — each distinct value enters a heap of size k.
* Space: **O(n)** — the map (plus the heap).

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0347/v1/TopKFrequent.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0347/v1/TopKFrequentTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle 9.8.2 project. Only a JDK is needed to start Gradle; JDK 25 is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-counting-bucket-sort](../v2-counting-bucket-sort/README.md): Counting + bucket sort (`O(n)` time, `O(n)` space)
