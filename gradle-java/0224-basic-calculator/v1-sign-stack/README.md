# 224. Basic Calculator — v1: Sign stack

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/basic-calculator/)

## Problem

Evaluate a valid expression string `s` containing non-negative integers, `+`, `-`, parentheses and spaces. `-` may also be unary
(e.g. `"-(2 + 3)"`). Do not use `eval`.

**Example 1**
```
Input:  s = "1 + 1"
Output: 2
```

**Example 2**
```
Input:  s = " 2-1 + 2 "
Output: 3
```

**Example 3**
```
Input:  s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

**Constraints**
* `1 <= s.length <= 3 * 10^5`; the result and intermediate values fit in 32-bit integers.

## Approach: Sign stack

> Keep a running result and sign; on '(' push them and start fresh, on ')' fold the inner result back in.

**Result + sign, with a stack for parentheses.** Read numbers digit by digit; on `+`/`-` add `sign * number` to `result` and set the
next sign. On `(`, push the current `result` and `sign`, then reset both. On `)`, finish the inner number, then
`result = pushedResult + pushedSign * result`.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the stack grows with parenthesis depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0224/v1/BasicCalculator.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0224/v1/BasicCalculatorTest.java` | JUnit 6 tests |
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
