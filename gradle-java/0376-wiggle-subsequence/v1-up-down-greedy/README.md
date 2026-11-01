# 376. Wiggle Subsequence — v1: Up/down greedy

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/wiggle-subsequence/)

## Problem

A **wiggle sequence** has differences that strictly alternate between positive and negative (a single element, or two different
elements, also count). Return the length of the longest wiggle **subsequence** of `nums`.

**Example**
```
[1,7,4,9,2,5]               → 6
[1,17,5,10,13,15,10,5,16,8] → 7
[1,2,3,4,5,6,7,8,9]         → 2
```

**Constraints**
* `1 <= nums.length <= 1000`

## Approach: Up/down greedy

> Track the longest wiggle ending with a rise and the longest ending with a fall.

**Two counters.** `up` is the longest wiggle so far ending with a rise, `down` the longest ending with a fall. A rise extends a sequence
that last fell: `up = down + 1`; a fall sets `down = up + 1`; equal neighbours change nothing. This is the same as counting the turning
points of the sequence.

* Time: **O(n)** — one pass.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0376/v1/WiggleSubsequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0376/v1/WiggleSubsequenceTest.java` | JUnit 6 tests |
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
