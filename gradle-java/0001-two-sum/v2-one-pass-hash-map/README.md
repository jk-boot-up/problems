# 1. Two Sum — v2: One-pass hash map

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/two-sum/)

## Problem

Given an integer array `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.
Exactly one solution exists, and you may not use the same element twice. Return the indices in any order.

**Example 1**
```
Input:  nums = [2,7,11,15], target = 9
Output: [0,1]
```

**Example 2**
```
Input:  nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3**
```
Input:  nums = [3,3], target = 6
Output: [0,1]
```

**Constraints**
* `2 <= nums.length <= 10^4`; `-10^9 <= nums[i], target <= 10^9`

**Follow-up:** better than O(n²)?

## Approach: One-pass hash map

> As you scan, look up target − x among the values already seen; a hash map makes that lookup O(1).

**Hash map of seen values.** For each `nums[i]`, check whether `target - nums[i]` was seen earlier; if so, return both indices.
Otherwise store `nums[i] → i`.

* Time: **O(n)** — one pass with O(1) average lookups.
* Space: **O(n)** — the map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0001/v2/TwoSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0001/v2/TwoSumTest.java` | JUnit 6 tests |
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

* [v1-brute-force](../v1-brute-force/README.md): Brute force (`O(n²)` time, `O(1)` space)
