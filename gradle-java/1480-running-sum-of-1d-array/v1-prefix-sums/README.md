# 1480. Running Sum of 1d Array — v1: Prefix sums

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/)

## Problem

Return the running sum: `runningSum[i] = nums[0] + … + nums[i]`.

**Example**
```
[1,2,3,4] → [1,3,6,10],   [1,1,1,1,1] → [1,2,3,4,5]
```

**Constraints**
* `1 <= nums.length <= 1000`

## Approach: Prefix sums

> Each prefix sum is the previous prefix sum plus the current value.

**One pass.** `out[i] = out[i-1] + nums[i]`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1480/v1/RunningSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1480/v1/RunningSumTest.java` | JUnit 6 tests |
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
