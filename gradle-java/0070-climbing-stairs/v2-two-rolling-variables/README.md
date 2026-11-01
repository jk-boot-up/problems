# 70. Climbing Stairs — v2: Two rolling variables

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/climbing-stairs/)

## Problem

You climb a staircase of `n` steps, taking 1 or 2 steps at a time. In how many distinct ways can you reach the top?

**Example**
```
n = 2 → 2 (1+1, 2),   n = 3 → 3 (1+1+1, 1+2, 2+1)
```

**Constraints**
* `1 <= n <= 45`

## Approach: Two rolling variables

> ways(n) = ways(n − 1) + ways(n − 2): the last move was either one step or two.

**Fibonacci recurrence.** `ways(1) = 1`, `ways(2) = 2`, and `ways(i) = ways(i-1) + ways(i-2)`. Only the last two values are needed.

* Time: **O(n)** — one loop.
* Space: **O(1)** — two variables.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0070/v2/ClimbingStairs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0070/v2/ClimbingStairsTest.java` | JUnit 6 tests |
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

* [v1-memoized-recursion](../v1-memoized-recursion/README.md): Memoized recursion (`O(n)` time, `O(n)` space)
