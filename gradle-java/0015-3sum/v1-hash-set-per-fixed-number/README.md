# 15. 3Sum — v1: Hash set per fixed number

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/3sum/)

## Problem

Return all **unique** triplets `[a, b, c]` from `nums` (at different indices) with `a + b + c == 0`. The answer must not
contain duplicate triplets; order does not matter.

**Example 1**
```
Input:  nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2**
```
Input:  nums = [0,1,1]
Output: []
```

**Example 3**
```
Input:  nums = [0,0,0]
Output: [[0,0,0]]
```

**Constraints**
* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

## Approach: Hash set per fixed number

> Fix nums[i]; scan the rest with a hash set looking for the value that completes the triplet.

**Hashing.** Sort (so triplets come out in a canonical order), then for each `i` scan `j > i` with a set of seen values:
if `-(nums[i] + nums[j])` was seen, record the triplet. A `Set<List<Integer>>` removes duplicates.

* Time: **O(n²)** — n fixed values × a linear scan.
* Space: **O(n)** — the seen set (plus the output).

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0015/v1/ThreeSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0015/v1/ThreeSumTest.java` | JUnit 6 tests |
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

* [v2-sort-two-pointers](../v2-sort-two-pointers/README.md): Sort + two pointers (`O(n²)` time, `O(1)` space)
