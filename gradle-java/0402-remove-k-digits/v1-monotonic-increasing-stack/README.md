# 402. Remove K Digits — v1: Monotonic increasing stack

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Monotonic Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-k-digits/)

## Problem

Given a non-negative integer as a string `num` and an integer `k`, remove `k` digits so the remaining number is as small as possible.
Return it without leading zeros (`"0"` if nothing is left).

**Example**
```
num = "1432219", k = 3 → "1219"
num = "10200",   k = 1 → "200"
num = "10",      k = 2 → "0"
```

**Constraints**
* `1 <= k <= num.length <= 10^5`; `num` has no leading zeros except `"0"` itself

## Approach: Monotonic increasing stack

> Scan left to right; whenever a digit is smaller than the one before it, removing the bigger one earlier helps most.

**Greedy with a stack.** A smaller digit should move as far left as possible. Push digits onto a stack; before pushing `d`, pop larger
digits while removals remain. Leftover removals come off the end (the stack is then non-decreasing, so the tail is the largest). Finally
strip leading zeros.

* Time: **O(n)** — each digit is pushed and popped at most once.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0402/v1/RemoveKDigits.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0402/v1/RemoveKDigitsTest.java` | JUnit 6 tests |
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
