# 227. Basic Calculator II — v1: Stack of terms

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/basic-calculator-ii/)

## Problem

Evaluate an expression string containing non-negative integers, `+ - * /` and spaces. Integer division truncates toward zero. The
expression is always valid and every intermediate value fits in 32 bits. Do not use `eval`.

**Example**
```
"3+2*2"      → 7
" 3/2 "      → 1
" 3+5 / 2 "  → 5
```

**Constraints**
* `1 <= s.length <= 3 * 10^5`

## Approach: Stack of terms

> Push each term (negated for −, combined with the top for * and /) and sum the stack at the end.

**Stack.** Read a number, then apply the operator before it: push `num` for `+`, `-num` for `-`, and replace the top with `top * num` or
`top / num` for `*` and `/`. The answer is the sum of the stack.

* Time: **O(n)** — one pass plus the final sum.
* Space: **O(n)** — up to one stacked term per number.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0227/v1/BasicCalculatorII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0227/v1/BasicCalculatorIITest.java` | JUnit 6 tests |
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

* [v2-running-sum-with-the-last-term](../v2-running-sum-with-the-last-term/README.md): Running sum with the last term (`O(n)` time, `O(1)` space)
