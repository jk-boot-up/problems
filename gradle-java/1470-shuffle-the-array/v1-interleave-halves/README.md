# 1470. Shuffle the Array — v1: Interleave halves

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/shuffle-the-array/)

## Problem

Given `nums = [x1,…,xn,y1,…,yn]`, return `[x1,y1,x2,y2,…,xn,yn]`.

**Example**
```
nums = [2,5,1,3,4,7], n = 3 → [2,3,5,4,1,7]
```

**Constraints**
* `1 <= n <= 500`

## Approach: Interleave halves

> Element i of the first half and element i of the second half go to positions 2i and 2i + 1.

**Direct placement.** `out[2i] = nums[i]` and `out[2i + 1] = nums[n + i]`.

* Time: **O(n)**.
* Space: **O(n)** — the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1470/v1/ShuffleTheArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1470/v1/ShuffleTheArrayTest.java` | JUnit 6 tests |
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
