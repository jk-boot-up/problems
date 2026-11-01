# 287. Find the Duplicate Number — v1: Seen set

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/)

## Problem

`nums` has `n + 1` integers, each in `[1, n]`. Exactly one value is repeated (possibly many times). Return it without modifying the
array and using O(1) extra space.

**Example**
```
[1,3,4,2,2] → 2,   [3,1,3,4,2] → 3,   [3,3,3,3,3] → 3
```

**Constraints**
* `1 <= n <= 10^5`

## Approach: Seen set

> Remember every value; the first one seen twice is the duplicate.

**`MyHashSet`.** Simple, but uses O(n) memory, which the problem forbids.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0287/v1/FindDuplicate.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0287/v1/FindDuplicateTest.java` | JUnit 6 tests |
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

* [v2-floyd-cycle-detection](../v2-floyd-cycle-detection/README.md): Floyd cycle detection (`O(n)` time, `O(1)` space)
