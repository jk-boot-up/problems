# 1365. How Many Numbers Are Smaller Than the Current Number — v1: Counting sort prefix sums

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

## Problem

For each `nums[i]`, return how many other values in `nums` are strictly smaller.

**Example**
```
[8,1,2,2,3] → [4,0,1,1,3],   [6,5,4,8] → [2,1,0,3],   [7,7,7,7] → [0,0,0,0]
```

**Constraints**
* `2 <= nums.length <= 500`; `0 <= nums[i] <= 100`

## Approach: Counting sort prefix sums

> Values are small (0–100): count them, then prefix-sum the counts.

**Counting.** `count[v]` holds how many times `v` appears; turn it into "how many values are less than v" with a running sum.

* Time: **O(n + R)** — R = 101 possible values.
* Space: **O(R)** — the count array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1365/v1/SmallerThanCurrent.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1365/v1/SmallerThanCurrentTest.java` | JUnit 6 tests |
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
