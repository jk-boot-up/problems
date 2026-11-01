# 128. Longest Consecutive Sequence — v2: Hash set, count from run starts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)

## Problem

Given an unsorted integer array `nums`, return the length of the longest run of consecutive integers (e.g. 1, 2, 3, 4) that can be
formed from its values. Your algorithm must run in **O(n)** time.

**Example 1**
```
Input:  nums = [100,4,200,1,3,2]
Output: 4   (1, 2, 3, 4)
```

**Example 2**
```
Input:  nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

**Constraints**
* `0 <= nums.length <= 10^5`; `-10^9 <= nums[i] <= 10^9`

## Approach: Hash set, count from run starts

> Put everything in a set; only start counting from numbers whose predecessor is missing.

**Run starts only.** Put all values in a hash set (our own `MyHashSet`). A value `x` starts a run if `x - 1` is not in the set. Only from such starts,
count `x + 1, x + 2, …` while present. Each value is visited by at most one counting walk.

* Time: **O(n)** — every value is counted at most once across all runs.
* Space: **O(n)** — the set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0128/v2/LongestConsecutiveSequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0128/v2/LongestConsecutiveSequenceTest.java` | JUnit 6 tests |
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

* [v1-sort-and-scan](../v1-sort-and-scan/README.md): Sort and scan (`O(n log n)` time, `O(log n)` space)
