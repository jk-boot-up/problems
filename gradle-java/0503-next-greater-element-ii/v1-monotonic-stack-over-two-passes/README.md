# 503. Next Greater Element II — v1: Monotonic stack over two passes

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/next-greater-element-ii/)

## Problem

`nums` is **circular**. For each element, return the first greater value found by moving right (wrapping around), or `-1`.

**Example**
```
[1,2,1] → [2,-1,2],   [1,2,3,4,3] → [2,3,4,-1,4]
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: Monotonic stack over two passes

> Scan the circular array twice with a stack of indices; the second pass resolves elements that wrap around.

**Virtual doubled array.** Iterate `i` from 0 to `2n - 1` using `nums[i % n]`; pop smaller indices from the stack and set their answer.
Only push indices during the first pass.

* Time: **O(n)** — each index is pushed and popped once.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0503/v1/NextGreaterElementII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0503/v1/NextGreaterElementIITest.java` | JUnit 6 tests |
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
