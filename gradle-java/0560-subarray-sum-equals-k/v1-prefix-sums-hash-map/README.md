# 560. Subarray Sum Equals K — v1: Prefix sums + hash map

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/)

## Problem

Return the number of contiguous subarrays of `nums` whose sum equals `k`.

**Example**
```
nums = [1,1,1], k = 2 → 2,   nums = [1,2,3], k = 3 → 2
```

**Constraints**
* `1 <= nums.length <= 2 * 10^4`; `-1000 <= nums[i] <= 1000`

## Approach: Prefix sums + hash map

> A subarray sums to k when two prefix sums differ by k; count earlier prefix sums in a hash map.

**Prefix-sum counting.** Let `sum` be the running total. A subarray ending here sums to `k` when an earlier prefix equals `sum - k`. Keep
how many times each prefix sum occurred in a `MyHashMap` (starting with `0 → 1`). Negative numbers make a sliding window impossible.

* Time: **O(n)** — one pass with O(1) map operations.
* Space: **O(n)** — the map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0560/v1/SubarraySumEqualsK.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0560/v1/SubarraySumEqualsKTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
