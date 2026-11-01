# 22. Generate Parentheses — v1: Backtracking with open/close counts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/generate-parentheses/)

## Problem

Given `n` pairs of parentheses, generate all combinations of **well-formed** parentheses.

**Example**
```
Input:  n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Constraints**
* `1 <= n <= 8`

## Approach: Backtracking with open/close counts

> Add '(' while some remain, and ')' only when it would close an open one.

**Track open and close counts.** Append `(` if `open < n`; append `)` if `close < open`. A string of length `2n` built this way is
always valid, and every valid string is reached exactly once.

* Time: **O(4ⁿ / √n)** — the number of valid strings (the Catalan number), each of length 2n.
* Space: **O(n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0022/v1/GenerateParentheses.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0022/v1/GenerateParenthesesTest.java` | JUnit 6 tests |
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
