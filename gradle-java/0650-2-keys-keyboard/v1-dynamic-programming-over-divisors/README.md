# 650. 2 Keys Keyboard — v1: Dynamic programming over divisors

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/2-keys-keyboard/)

## Problem

The screen starts with one `'A'`. Each step is either **Copy All** (copy everything on screen) or **Paste** (append the last copy). Return
the minimum number of steps to get exactly `n` letters.

**Example**
```
n = 3 → 3   (copy, paste, paste)
n = 1 → 0
n = 6 → 5   (copy, paste → 2; copy, paste, paste → 6)
```

**Constraints**
* `1 <= n <= 1000`

## Approach: Dynamic programming over divisors

> best[i] = min over divisors d of i of best[d] + i / d: reach d, then copy and paste up to i.

**DP.** To reach `i` the last copy happened at some length `d` dividing `i`; then one copy and `i/d - 1` pastes follow. So
`best[i] = min(best[d] + i / d)` over divisors `d < i`, with `best[1] = 0`.

* Time: **O(n²)** — trying every smaller length for each `i`.
* Space: **O(n)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0650/v1/TwoKeysKeyboard.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0650/v1/TwoKeysKeyboardTest.java` | JUnit 6 tests |
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

* [v2-sum-of-prime-factors](../v2-sum-of-prime-factors/README.md): Sum of prime factors (`O(√n)` time, `O(1)` space)
