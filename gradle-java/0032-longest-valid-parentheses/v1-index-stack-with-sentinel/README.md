# 32. Longest Valid Parentheses — v1: Index stack with sentinel

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-valid-parentheses/)

## Problem

Given a string of `'('` and `')'`, return the length of the longest **well-formed** (valid) parentheses substring.

**Example**
```
"(()" → 2,   ")()())" → 4,   "" → 0
```

**Constraints**
* `0 <= s.length <= 3 * 10^4`

## Approach: Index stack with sentinel

> Keep a stack of indices with a sentinel for the last unmatched ')'; each match measures a valid stretch.

**Index stack.** Push `-1` as a base. Push the index of each `'('`. For `')'`, pop: if the stack becomes empty this `')'` is unmatched, so
push its index as the new base; otherwise the valid stretch ends here and starts after the index now on top: `i - top`.

* Time: **O(n)** — each index is pushed and popped at most once.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0032/v1/LongestValidParentheses.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0032/v1/LongestValidParenthesesTest.java` | JUnit 6 tests |
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
