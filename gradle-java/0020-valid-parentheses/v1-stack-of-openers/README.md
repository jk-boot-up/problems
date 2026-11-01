# 20. Valid Parentheses — v1: Stack of openers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-parentheses/)

## Problem

Given a string `s` of the characters `()[]{}`, decide whether it is **valid**: every opening bracket is closed by the same type of
bracket, in the correct order, and every closing bracket has a matching opener.

**Example 1**
```
Input:  s = "()[]{}"
Output: true
```

**Example 2**
```
Input:  s = "(]"
Output: false
```

**Example 3**
```
Input:  s = "([])"
Output: true
```

**Constraints**
* `1 <= s.length <= 10^4`; only `()[]{}`.

## Approach: Stack of openers

> Push every opener; each closer must match the opener on top of the stack.

**Stack.** Push the expected closer for every opener. For a closer, the stack must be non-empty and its top must equal that closer.
At the end the stack must be empty.

* Time: **O(n)** — each character is pushed or popped once.
* Space: **O(n)** — the stack in the worst case (all openers).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0020/v1/ValidParentheses.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0020/v1/ValidParenthesesTest.java` | JUnit 6 tests |
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
