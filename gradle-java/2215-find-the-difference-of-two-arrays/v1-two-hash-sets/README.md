# 2215. Find the Difference of Two Arrays — v1: Two hash sets

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-difference-of-two-arrays/)

## Problem

Return `[a, b]` where `a` holds the distinct values of `nums1` not in `nums2`, and `b` the distinct values of `nums2` not in `nums1`
(any order).

**Example**
```
nums1 = [1,2,3], nums2 = [2,4,6] → [[1,3],[4,6]]
```

**Constraints**
* `1 <= nums1.length, nums2.length <= 1000`

## Approach: Two hash sets

> Put each array in a hash set; keep the distinct values missing from the other set.

**Sets.** Build `MyHashSet`s of both arrays, then collect each set's values that the other lacks.

* Time: **O(m + n)** — linear set operations.
* Space: **O(m + n)** — the sets.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p2215/v1/DifferenceOfTwoArrays.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p2215/v1/DifferenceOfTwoArraysTest.java` | JUnit 6 tests |
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
