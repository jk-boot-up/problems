# 322. Coin Change — v1: Top-down memoized recursion

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/coin-change/)

## Problem

Given coin denominations `coins` (unlimited supply of each) and an `amount`, return the fewest coins that add up to `amount`, or `-1`
if it is impossible.

**Example**
```
coins = [1,2,5], amount = 11 → 3 (5 + 5 + 1)
coins = [2],     amount = 3  → -1
coins = [1],     amount = 0  → 0
```

**Constraints**
* `1 <= coins.length <= 12`; `1 <= coins[i] <= 2^31 - 1`; `0 <= amount <= 10^4`

## Approach: Top-down memoized recursion

> minCoins(a) = 1 + min over coins of minCoins(a − coin), with answers cached in an array.

**Memoized recursion.** `solve(a)`: 0 for `a == 0`, -1 for `a < 0`, otherwise try every coin; cache results in `memo[a]`.

* Time: **O(amount · coins)** — each amount is solved once, trying every coin.
* Space: **O(amount)** — the memo array and the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0322/v1/CoinChange.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0322/v1/CoinChangeTest.java` | JUnit 6 tests |
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

* [v2-bottom-up-dp](../v2-bottom-up-dp/README.md): Bottom-up DP (`O(amount · coins)` time, `O(amount)` space)
