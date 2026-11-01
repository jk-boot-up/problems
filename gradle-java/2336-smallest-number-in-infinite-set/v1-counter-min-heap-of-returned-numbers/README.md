# 2336. Smallest Number in Infinite Set — v1: Counter + min-heap of returned numbers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/smallest-number-in-infinite-set/)

## Problem

The set initially contains every positive integer. Implement:
* `popSmallest()`: remove and return the smallest number;
* `addBack(num)`: put `num` back if it is not already in the set.

**Example**
```
addBack(2); popSmallest() → 1; popSmallest() → 2; popSmallest() → 3;
addBack(1); popSmallest() → 1; popSmallest() → 4; popSmallest() → 5
```

**Constraints**
* `1 <= num <= 1000`; at most 1000 calls.

## Approach: Counter + min-heap of returned numbers

> Numbers from 'next' upward are implicitly present; returned numbers below 'next' live in a min-heap (with a set to avoid duplicates).

**Two parts.** `next` is the smallest number never popped; everything from `next` upward is present. Numbers added back below `next` go into a
min-heap, with a `MyHashSet` to prevent duplicates. `popSmallest` takes from the heap if it is not empty, otherwise returns `next++`.

* Time: **O(log n)** — per operation.
* Space: **O(n)** — the heap and set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p2336/v1/SmallestInfiniteSet.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p2336/v1/SmallestInfiniteSetTest.java` | JUnit 6 tests |
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
