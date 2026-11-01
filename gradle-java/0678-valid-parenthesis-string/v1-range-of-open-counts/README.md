# 678. Valid Parenthesis String — v1: Range of open counts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/)

## Problem

`s` contains `(`, `)` and `*`, where `*` can be `(`, `)` or empty. Return `true` if some choice makes `s` a valid parentheses string.

**Example**
```
"()" → true,   "(*)" → true,   "(*))" → true,   ")(" → false
```

**Constraints**
* `1 <= s.length <= 100`

## Approach: Range of open counts

> Track the range [lo, hi] of possible open-bracket counts; '*' widens the range.

**Interval of open counts.** `lo` is the fewest open brackets possible, `hi` the most. `(` raises both, `)` lowers both, `*` lowers `lo` and
raises `hi`. If `hi < 0`, too many `)` appear: fail. Clamp `lo` at 0. At the end, valid iff `lo == 0`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0678/v1/ValidParenthesisString.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0678/v1/ValidParenthesisStringTest.java` | JUnit 6 tests |
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
