# 645. Set Mismatch — v1: Counting array

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/set-mismatch/)

## Problem

A set held `1..n`, but one number was duplicated, replacing another. Given the resulting array `nums`, return `[duplicate, missing]`.

**Example**
```
[1,2,2,4] → [2,3],   [1,1] → [1,2]
```

**Constraints**
* `2 <= n <= 10^4`

## Approach: Counting array

> Count occurrences of 1..n: the value seen twice is the duplicate, the value seen zero times is missing.

**Counts.** `count[v]` for each value; the one with count 2 is the duplicate, the one with count 0 is missing.

* Time: **O(n)** — two passes.
* Space: **O(n)** — the count array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0645/v1/SetMismatch.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0645/v1/SetMismatchTest.java` | JUnit 6 tests |
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
