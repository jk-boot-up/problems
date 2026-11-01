# 279. Perfect Squares — v1: DP over amounts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/perfect-squares/)

## Problem

Return the least number of perfect squares (`1, 4, 9, 16, …`) that sum to `n`.

**Example**
```
12 → 3 (4 + 4 + 4),   13 → 2 (4 + 9)
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: DP over amounts

> dp[n] = 1 + min over squares s ≤ n of dp[n − s]: the last square used, plus the best way to make the rest.

**Coin change with square coins.** `dp[0] = 0`; for each `i`, try every square `j² <= i`: `dp[i] = min(dp[i], dp[i - j²] + 1)`.

* Time: **O(n·√n)** — √n squares for each amount.
* Space: **O(n)** — the dp array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0279/v1/PerfectSquares.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0279/v1/PerfectSquaresTest.java` | JUnit 6 tests |
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
