# 84. Largest Rectangle in Histogram — v1: Monotonic stack

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Problem

Bars of width 1 have heights `heights[i]`. Return the area of the largest rectangle that fits inside the histogram.

**Example**
```
[2,1,5,6,2,3] → 10   (heights 5 and 6, width 2)
[2,4]         → 4
```

**Constraints**
* `1 <= heights.length <= 10^5`; `0 <= heights[i] <= 10^4`

## Approach: Monotonic stack

> A monotonic stack of increasing bars; when a shorter bar arrives, each popped bar's widest rectangle is known.

**Increasing stack.** Push indices while heights increase. When `heights[i]` is lower than the top, pop the top bar: its rectangle can
extend right up to `i - 1` and left past the new top, so `width = i - newTop - 1`. A final height-0 sentinel flushes the stack.

* Time: **O(n)** — each bar is pushed and popped once.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0084/v1/LargestRectangleHistogram.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0084/v1/LargestRectangleHistogramTest.java` | JUnit 6 tests |
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
