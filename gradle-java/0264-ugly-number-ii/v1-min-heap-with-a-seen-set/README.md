# 264. Ugly Number II — v1: Min-heap with a seen set

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ugly-number-ii/)

## Problem

Return the `n`-th ugly number (prime factors only 2, 3 and 5; the sequence starts `1, 2, 3, 4, 5, 6, 8, 9, 10, 12, …`).

**Example**
```
n = 10 → 12
n = 1  → 1
```

**Constraints**
* `1 <= n <= 1690`

## Approach: Min-heap with a seen set

> Pop the smallest ugly number and push its ×2, ×3, ×5 multiples, skipping ones already queued.

**Heap.** Start the heap with 1. Pop `n` times; after each pop push `x·2`, `x·3`, `x·5` unless they are already in a `MyHashSet`. The
`n`-th pop is the answer. Use `long`, since multiples can pass `2^31`.

* Time: **O(n log n)** — `3n` pushes into a heap of size `O(n)`.
* Space: **O(n)** — the heap and the set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0264/v1/UglyNumberII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0264/v1/UglyNumberIITest.java` | JUnit 6 tests |
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

* [v2-three-pointers](../v2-three-pointers/README.md): Three pointers (`O(n)` time, `O(n)` space)
