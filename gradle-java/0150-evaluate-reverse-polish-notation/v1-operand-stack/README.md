# 150. Evaluate Reverse Polish Notation — v1: Operand stack

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

## Problem

Evaluate an arithmetic expression in **Reverse Polish Notation** given as `tokens`. Operators are `+ - * /`; each operand is an
integer or a sub-expression. Division truncates toward zero. The expression is always valid and fits in 32-bit integers.

**Example 1**
```
Input:  tokens = ["2","1","+","3","*"]
Output: 9   ((2 + 1) * 3)
```

**Example 2**
```
Input:  tokens = ["4","13","5","/","+"]
Output: 6   (4 + 13 / 5)
```

**Constraints**
* `1 <= tokens.length <= 10^4`

## Approach: Operand stack

> Numbers go on a stack; an operator pops two operands, applies itself and pushes the result.

**Stack.** Push numbers. For an operator, pop `b` then `a` (note the order), push `a op b`. The final stack holds the answer.

* Time: **O(n)** — one pass.
* Space: **O(n)** — the operand stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0150/v1/EvaluateRPN.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0150/v1/EvaluateRPNTest.java` | JUnit 6 tests |
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
