# 155. Min Stack — v1: Value-and-minimum pairs

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/min-stack/)

## Problem

Design a stack that supports `push(val)`, `pop()`, `top()` and `getMin()` (the smallest element in the stack), each in **O(1)** time.
`pop`, `top` and `getMin` are only called on a non-empty stack.

**Example**
```
push(-2), push(0), push(-3)
getMin() → -3
pop()
top()    → 0
getMin() → -2
```

**Constraints**
* `-2^31 <= val <= 2^31 - 1`; at most `3 * 10^4` calls.

## Approach: Value-and-minimum pairs

> Store, with every pushed value, the minimum of the stack at that moment.

**Pairs.** Each stack entry is `(value, minSoFar)` where `minSoFar = min(value, previous top's minSoFar)`. Popping restores the previous
minimum automatically, because it is stored in the entry below.

* Time: **O(1)** — every operation touches only the top.
* Space: **O(n)** — two numbers per element.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0155/v1/MinStack.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0155/v1/MinStackTest.java` | JUnit 6 tests |
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
