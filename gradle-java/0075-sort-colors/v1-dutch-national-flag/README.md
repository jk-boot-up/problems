# 75. Sort Colors — v1: Dutch national flag

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sort-colors/)

## Problem

`nums` holds only `0`, `1` and `2` (red, white, blue). Sort it **in place** so equal colours are adjacent in that order, without a
library sort.

**Example**
```
[2,0,2,1,1,0] → [0,0,1,1,2,2]
```

**Constraints**
* `1 <= n <= 300`

**Follow-up:** one pass, constant space.

## Approach: Dutch national flag

> Dutch national flag: three regions (0s, 1s, 2s) grow from both ends in one pass.

**Three pointers.** `lo` is the end of the 0s, `hi` the start of the 2s, `i` the scanner. A 0 swaps to `lo` (both advance), a 2
swaps to `hi` (only `hi` moves, the swapped-in value still needs checking), a 1 just advances `i`.

* Time: **O(n)** — each element is examined at most twice.
* Space: **O(1)** — three indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0075/v1/SortColors.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0075/v1/SortColorsTest.java` | JUnit 6 tests |
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
