# 128. Longest Consecutive Sequence — v1: Sort and scan

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

## Approach: Sort and scan

> After sorting, consecutive values sit next to each other.

**Sort.** Sort, then scan: extend the run when `a[i] == a[i-1] + 1`, ignore duplicates, and reset otherwise.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0128/v1/LongestConsecutiveSequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0128/v1/LongestConsecutiveSequenceTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-hash-set-count-from-run-starts](../v2-hash-set-count-from-run-starts/README.md): Hash set, count from run starts (`O(n)` time, `O(n)` space)
