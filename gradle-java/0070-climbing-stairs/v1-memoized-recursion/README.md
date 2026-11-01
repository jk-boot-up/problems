# 70. Climbing Stairs — v1: Memoized recursion

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/climbing-stairs/)

## Problem

You climb a staircase of `n` steps, taking 1 or 2 steps at a time. In how many distinct ways can you reach the top?

**Example**
```
n = 2 → 2 (1+1, 2),   n = 3 → 3 (1+1+1, 1+2, 2+1)
```

**Constraints**
* `1 <= n <= 45`

## Approach: Memoized recursion

> Recurse on n − 1 and n − 2, caching each answer so it is computed only once.

**Top-down with a memo array.** `ways(n) = ways(n-1) + ways(n-2)`, storing results in `memo[n]`.

* Time: **O(n)** — each n is computed once.
* Space: **O(n)** — the memo array and the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0070/v1/ClimbingStairs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0070/v1/ClimbingStairsTest.java` | JUnit 6 tests |
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

* [v2-two-rolling-variables](../v2-two-rolling-variables/README.md): Two rolling variables (`O(n)` time, `O(1)` space)
