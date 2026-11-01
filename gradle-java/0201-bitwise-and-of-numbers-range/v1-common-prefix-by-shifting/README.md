# 201. Bitwise AND of Numbers Range — v1: Common prefix by shifting

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

## Problem

Return the bitwise AND of all integers in the inclusive range `[left, right]`.

**Example**
```
[5, 7] → 4,   [0, 0] → 0,   [1, 2147483647] → 0
```

**Constraints**
* `0 <= left <= right <= 2^31 - 1`

## Approach: Common prefix by shifting

> Only the common binary prefix of left and right survives; every lower bit flips somewhere in the range.

**Shift until equal.** While `left != right`, shift both right and count the shifts. The remaining value is the common prefix; shift it
back left. Any bit below the prefix is 0 for at least one number in the range.

* Time: **O(1)** — at most 31 shifts.
* Space: **O(1)** — a shift counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0201/v1/RangeBitwiseAnd.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0201/v1/RangeBitwiseAndTest.java` | JUnit 6 tests |
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
