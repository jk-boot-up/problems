# 282. Expression Add Operators — v1: Backtracking with the last operand

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/expression-add-operators/)

## Problem

Given a digit string `num` and an integer `target`, insert `+`, `-` or `*` between digits (or nothing, to join digits into one number) and
return every expression that evaluates to `target`. Numbers must not have leading zeros (`"05"` is not allowed, `"0"` is).

**Example**
```
num = "123", target = 6   → ["1*2*3","1+2+3"]
num = "232", target = 8   → ["2*3+2","2+3*2"]
num = "105", target = 5   → ["1*0+5","10-5"]
num = "3456237490", target = 9191 → []
```

**Constraints**
* `1 <= num.length <= 10`, `-2^31 <= target <= 2^31 - 1`

## Approach: Backtracking with the last operand

> Backtrack over where numbers end and which operator joins them; remember the last term so * can undo it.

**Track the last term.** Choose the next number `cur = num[pos..i]`, then try each operator. For `+` and `-` the value changes by `±cur` and
the last term becomes `±cur`. For `*`, multiplication binds tighter, so undo the last term and apply it multiplied:
`value - last + last * cur`, with the new last term `last * cur`. Stop extending a number that starts with `0`. Use `long`.

* Time: **O(4ⁿ · n)** — up to 4 choices between digits, and building each expression.
* Space: **O(n)** — recursion depth and the expression buffer.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0282/v1/ExpressionAddOperators.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0282/v1/ExpressionAddOperatorsTest.java` | JUnit 6 tests |
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
