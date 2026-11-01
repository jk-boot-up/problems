# 2352. Equal Row and Column Pairs — v1: Hash rows, look up columns

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/equal-row-and-column-pairs/)

## Problem

Given an `n × n` grid, return the number of pairs `(r, c)` such that row `r` and column `c` contain the same values in the same order.

**Example**
```
[[3,2,1],[1,7,6],[2,7,7]]                 → 1
[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]] → 3
```

**Constraints**
* `1 <= n <= 200`

## Approach: Hash rows, look up columns

> Count each row (as a key) in a hash map, then look up every column.

**Row keys.** Turn each row into a `List<Integer>` and count it in a `MyHashMap`. For each column, build the same kind of key and add the
number of equal rows.

* Time: **O(n²)** — every cell is read twice; hashing a key costs O(n), n times per side.
* Space: **O(n²)** — the stored row keys.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p2352/v1/EqualRowColumnPairs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p2352/v1/EqualRowColumnPairsTest.java` | JUnit 6 tests |
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
