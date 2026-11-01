# 496. Next Greater Element I — v1: Monotonic stack + hash map

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/next-greater-element-i/)

## Problem

`nums1` is a subset of `nums2` (all values distinct). For each `x` in `nums1`, find the first value to the right of `x` in `nums2` that is
greater than `x`, or `-1`.

**Example**
```
nums1 = [4,1,2], nums2 = [1,3,4,2] → [-1,3,-1]
nums1 = [2,4],   nums2 = [1,2,3,4] → [3,-1]
```

**Constraints**
* `1 <= nums1.length <= nums2.length <= 1000`

## Approach: Monotonic stack + hash map

> A decreasing stack over nums2 finds every element's next greater value; a hash map answers the queries from nums1.

**One stack pass.** Scan `nums2`; while the current value is larger than the stack top, the top's next greater value is the current one:
record it in a `MyHashMap`. Then answer `nums1` from the map (default -1).

* Time: **O(m + n)** — each value is pushed and popped once.
* Space: **O(n)** — the stack and map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0496/v1/NextGreaterElementI.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0496/v1/NextGreaterElementITest.java` | JUnit 6 tests |
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
