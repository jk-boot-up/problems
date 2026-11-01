# 343. Integer Break — v1: Dynamic programming

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

## Approach: Dynamic programming

> best[i] is the largest product for i; the first part j combines with either i − j itself or its best split.

**DP.** `best[i] = max over j in 1..i-1 of j * max(i - j, best[i - j])`: after taking a first part `j`, either keep the rest whole or
break it further.

* Time: **O(n²)** — `n` values, each trying `n` first parts.
* Space: **O(n)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0343/v1/IntegerBreak.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0343/v1/IntegerBreakTest.java` | JUnit 6 tests |
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

* [v2-greedy-threes](../v2-greedy-threes/README.md): Greedy threes (`O(n)` time, `O(1)` space)
