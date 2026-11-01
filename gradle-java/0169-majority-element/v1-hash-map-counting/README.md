# 169. Majority Element — v1: Hash map counting

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/majority-element/)

## Problem

Given an array `nums` of size `n`, return the **majority element**: the value that appears more than `⌊n / 2⌋` times.
You may assume a majority element always exists.

**Example 1**
```
Input:  nums = [3,2,3]
Output: 3
```

**Example 2**
```
Input:  nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints**
* `1 <= n <= 5 * 10^4`
* `-10^9 <= nums[i] <= 10^9`

**Follow-up:** solve it in linear time and O(1) space.

## Approach: Hash map counting

> Count every value in a hash map; return the first one whose count passes n / 2.

**Count occurrences.** Increment `count[x]` for each value; as soon as a count exceeds `n / 2`, that value is the answer.

* Time: **O(n)** — one pass with O(1) map updates.
* Space: **O(n)** — up to n distinct keys in the map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0169/v1/MajorityElement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0169/v1/MajorityElementTest.java` | JUnit 6 tests |
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

* [v2-sort-and-take-the-middle](../v2-sort-and-take-the-middle/README.md): Sort and take the middle (`O(n log n)` time, `O(log n)` space)
* [v3-boyer-moore-voting](../v3-boyer-moore-voting/README.md): Boyer–Moore voting (`O(n)` time, `O(1)` space)
