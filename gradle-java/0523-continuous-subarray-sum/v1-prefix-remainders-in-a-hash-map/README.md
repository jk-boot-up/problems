# 523. Continuous Subarray Sum — v1: Prefix remainders in a hash map

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/continuous-subarray-sum/)

## Problem

Return `true` if `nums` has a contiguous subarray of length **at least 2** whose sum is a multiple of `k` (0 counts as a multiple).

**Example**
```
nums = [23,2,4,6,7], k = 6  → true   ([2,4])
nums = [23,2,6,4,7], k = 6  → true   (whole array, 42)
nums = [23,2,6,4,7], k = 13 → false
```

**Constraints**
* `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^9`, `1 <= k <= 2^31 - 1`

## Approach: Prefix remainders in a hash map

> Two prefix sums with the same remainder mod k bracket a subarray whose sum is a multiple of k.

**Same remainder.** If `prefix[j] % k == prefix[i] % k` then `nums[i..j-1]` sums to a multiple of `k`. Record the **earliest** index of
each remainder in a `MyHashMap` (remainder 0 at index -1, for subarrays starting at 0); if a remainder repeats at least two positions
later, return `true`. Use `long` because the running value plus `nums[i]` can pass `2^31`.

* Time: **O(n)**.
* Space: **O(min(n, k))** — distinct remainders.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0523/v1/ContinuousSubarraySum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0523/v1/ContinuousSubarraySumTest.java` | JUnit 6 tests |
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
