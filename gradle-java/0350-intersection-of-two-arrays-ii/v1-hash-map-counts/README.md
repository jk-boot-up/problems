# 350. Intersection of Two Arrays II — v1: Hash map counts

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

## Problem

Return the intersection of `nums1` and `nums2`, where each value appears as many times as it shows in **both** arrays, in any order.

**Example**
```
[1,2,2,1], [2,2] → [2,2],   [4,9,5], [9,4,9,8,4] → [4,9]
```

**Constraints**
* `1 <= length <= 1000`

## Approach: Hash map counts

> Count nums1 in a hash map; each value of nums2 that still has a count left is matched once.

**Counting.** Count `nums1` in a `MyHashMap`. For each value of `nums2` with a positive count, output it and decrement the count.

* Time: **O(m + n)** — linear map operations.
* Space: **O(m)** — the map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0350/v1/IntersectionOfTwoArraysII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0350/v1/IntersectionOfTwoArraysIITest.java` | JUnit 6 tests |
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
