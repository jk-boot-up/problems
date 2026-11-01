# 347. Top K Frequent Elements — v2: Counting + bucket sort

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

## Approach: Counting + bucket sort

> Count with a hash map, then drop each value into a bucket indexed by its count and read buckets from the top.

**Bucket sort by frequency.** Count each value in a `MyHashMap`. A count is at most `n`, so put each value into `bucket[count]`.
Walk the buckets from `n` down to 1, collecting values until `k` are found.

* Time: **O(n)** — counting and bucketing are linear.
* Space: **O(n)** — the map and the buckets.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0347/v2/TopKFrequent.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0347/v2/TopKFrequentTest.java` | JUnit 6 tests |
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

* [v1-counting-min-heap-of-size-k](../v1-counting-min-heap-of-size-k/README.md): Counting + min-heap of size k (`O(n log k)` time, `O(n)` space)
