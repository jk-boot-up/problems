# 343. Integer Break — v2: Greedy threes

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/integer-break/)

## Problem

Break a positive integer `n` into the sum of **at least two** positive integers and maximise their product. Return that product.

**Example**
```
n = 2  → 1   (1 + 1)
n = 10 → 36  (3 + 3 + 4)
```

**Constraints**
* `2 <= n <= 58`

## Approach: Greedy threes

> Break into as many 3s as possible, using a 4 (= 2 + 2) instead of 3 + 1 at the end.

**Threes.** Any part `p >= 5` is better split (`2(p - 2) > p`), and `4 = 2 + 2` gives the same product, so parts are 2s and 3s. Three 2s
(product 8) lose to two 3s (product 9), so use as many 3s as possible, finishing with 2, 4 or nothing. `n = 2` and `n = 3` must still
split, giving `n - 1`.

* Time: **O(n)** — at most `n / 3` multiplications.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0343/v2/IntegerBreak.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0343/v2/IntegerBreakTest.java` | JUnit 6 tests |
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

* [v1-dynamic-programming](../v1-dynamic-programming/README.md): Dynamic programming (`O(n²)` time, `O(n)` space)
