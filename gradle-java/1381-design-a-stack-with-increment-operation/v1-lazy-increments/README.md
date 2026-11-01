# 1381. Design a Stack With Increment Operation — v1: Lazy increments

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-a-stack-with-increment-operation/)

## Problem

Implement `CustomStack`:

* `CustomStack(int maxSize)` — pushes beyond `maxSize` elements are ignored.
* `void push(int x)`, `int pop()` (returns `-1` when empty).
* `void increment(int k, int val)` — add `val` to the bottom `k` elements (all of them if fewer).

**Example**
```
CustomStack(3); push(1); push(2); pop() → 2; push(2); push(3); push(4) (ignored);
increment(5,100); increment(2,100); pop() → 103; pop() → 202; pop() → 201; pop() → -1
```

**Constraints**
* `1 <= maxSize, x, k <= 1000`; up to 1000 calls of each method

## Approach: Lazy increments

> Store pending increments lazily at the top affected index and pass them down when that element is popped.

**Lazy tags.** Keep `inc[i]`: an amount to be added to elements `0..i`. `increment(k, val)` adds `val` to `inc[min(k, size) - 1]` only.
When popping index `i`, return `stack[i] + inc[i]` and move `inc[i]` down to `inc[i - 1]`, since it also applies below.

* Time: **O(1)** — every operation.
* Space: **O(maxSize)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1381/v1/CustomStack.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1381/v1/CustomStackTest.java` | JUnit 6 tests |
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
