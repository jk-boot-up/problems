# 367. Valid Perfect Square — v1: Binary search on the root

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-perfect-square/)

## Problem

Return `true` if `num` is a perfect square, without using a built-in square root.

**Example**
```
16 → true
14 → false
```

**Constraints**
* `1 <= num <= 2^31 - 1`

## Approach: Binary search on the root

> Binary search for an integer whose square is exactly num.

**Search the root.** The root, if any, is between 1 and 46340 (`46341² > 2^31`). Binary search on that range, squaring `mid` as a
`long` and comparing with `num`.

* Time: **O(log n)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0367/v1/ValidPerfectSquare.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0367/v1/ValidPerfectSquareTest.java` | JUnit 6 tests |
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
