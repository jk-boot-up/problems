# 239. Sliding Window Maximum — v1: Monotonic deque

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sliding-window-maximum/)

## Problem

A window of size `k` slides over `nums` from left to right. Return the maximum of each window position.

**Example**
```
nums = [1,3,-1,-3,5,3,6,7], k = 3 → [3,3,5,5,6,7]
```

**Constraints**
* `1 <= k <= nums.length <= 10^5`

## Approach: Monotonic deque

> A deque keeps indices of decreasing values; the front is always the window maximum.

**Decreasing deque.** Before pushing index `i`, pop smaller values from the back: they can never be a maximum again. Pop the front
when it falls out of the window. Once the first window is complete, the front holds the maximum.

* Time: **O(n)** — each index enters and leaves the deque once.
* Space: **O(k)** — the deque.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0239/v1/SlidingWindowMaximum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0239/v1/SlidingWindowMaximumTest.java` | JUnit 6 tests |
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
