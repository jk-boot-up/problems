# 349. Intersection of Two Arrays — v1: Hash sets

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)

## Problem

Return the distinct values present in both `nums1` and `nums2`, in any order.

**Example**
```
[1,2,2,1], [2,2] → [2],   [4,9,5], [9,4,9,8,4] → [9,4]
```

**Constraints**
* `1 <= length <= 1000`

## Approach: Hash sets

> Put one array in a hash set; collect the other's values that are in it, each once.

**Set membership.** Load `nums1` into a `MyHashSet`. For each value of `nums2`, if `remove` succeeds, it is common and reported once.

* Time: **O(m + n)** — linear set operations.
* Space: **O(m)** — the set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0349/v1/IntersectionOfTwoArrays.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0349/v1/IntersectionOfTwoArraysTest.java` | JUnit 6 tests |
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
