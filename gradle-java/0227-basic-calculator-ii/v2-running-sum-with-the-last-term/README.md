# 227. Basic Calculator II — v2: Running sum with the last term

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

## Approach: Running sum with the last term

> Keep a running sum plus the last term; * and / only change the last term.

**No stack needed.** `*` and `/` bind tighter, so they only ever change the most recent term. Keep `result` (all finished terms) and
`last` (the term being built). When an operator ends a number: for `+`/`-`, fold `last` into `result` and start a new term `±num`; for
`*`/`/`, update `last` in place. A sentinel `+` at the end flushes the final number.

* Time: **O(n)** — one pass.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0227/v2/BasicCalculatorII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0227/v2/BasicCalculatorIITest.java` | JUnit 6 tests |
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

* [v1-stack-of-terms](../v1-stack-of-terms/README.md): Stack of terms (`O(n)` time, `O(n)` space)
