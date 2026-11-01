# 518. Coin Change II — v1: Unbounded knapsack counting

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/coin-change-ii/)

## Problem

Return the number of **combinations** of coins (unlimited supply) that make up `amount`. Order does not matter.

**Example**
```
amount = 5, coins = [1,2,5] → 4,   amount = 3, coins = [2] → 0,   amount = 10, coins = [10] → 1
```

**Constraints**
* `0 <= amount <= 5000`; `1 <= coins.length <= 300`

## Approach: Unbounded knapsack counting

> Loop coins on the outside so each combination is counted once, in a fixed coin order.

**Coins outer, amounts inner.** `ways[0] = 1`. For each coin `c`, for `a` from `c` up to `amount`: `ways[a] += ways[a - c]`. Because
coins are processed one at a time, `1+2` and `2+1` are not both counted.

* Time: **O(coins · amount)** — every pair.
* Space: **O(amount)** — one array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0518/v1/CoinChangeII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0518/v1/CoinChangeIITest.java` | JUnit 6 tests |
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
