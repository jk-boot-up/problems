# 1004. Max Consecutive Ones III — v1: Sliding window with a zero budget

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)

## Problem

Given a binary array and an integer `k`, return the longest run of `1`s you can get by flipping at most `k` zeros.

**Example**
```
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2 → 6
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3 → 10
```

**Constraints**
* `1 <= nums.length <= 10^5`; `0 <= k <= nums.length`

## Approach: Sliding window with a zero budget

> Keep a window with at most k zeros (the zeros you would flip); shrink from the left when it has too many.

**Window with ≤ k zeros.** Extend the right edge; count zeros inside. While the count exceeds `k`, move the left edge past a zero. The window
length is a candidate answer.

* Time: **O(n)** — each index enters and leaves once.
* Space: **O(1)** — a counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1004/v1/MaxConsecutiveOnesIII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1004/v1/MaxConsecutiveOnesIIITest.java` | JUnit 6 tests |
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
