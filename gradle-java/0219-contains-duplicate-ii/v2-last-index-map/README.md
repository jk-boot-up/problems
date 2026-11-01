# 219. Contains Duplicate II — v2: Last-index map

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)

## Problem

Return `true` if there are two **distinct** indices `i` and `j` with `nums[i] == nums[j]` and `|i - j| <= k`.

**Example 1**
```
Input:  nums = [1,2,3,1], k = 3
Output: true
```

**Example 2**
```
Input:  nums = [1,0,1,1], k = 1
Output: true
```

**Example 3**
```
Input:  nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Constraints**
* `1 <= nums.length <= 10^5`; `0 <= k <= 10^5`

## Approach: Last-index map

> Remember the last index of every value; a repeat within k positions answers true.

**Last occurrence.** Map each value to the last index where it appeared. At index `i`, if `nums[i]` was seen at `j` with
`i - j <= k`, return `true`; then update the map.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the map of distinct values.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0219/v2/ContainsDuplicateII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0219/v2/ContainsDuplicateIITest.java` | JUnit 6 tests |
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

* [v1-check-the-next-k-values](../v1-check-the-next-k-values/README.md): Check the next k values (`O(n·k)` time, `O(1)` space)
