# 18. 4Sum — v1: Sort + two loops + two pointers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/4sum/)

## Problem

Return all unique quadruplets `[a, b, c, d]` from `nums` (distinct indices) whose sum equals `target`, in any order.

**Example**
```
nums = [1,0,-1,0,-2,2], target = 0 → [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
nums = [2,2,2,2,2], target = 8      → [[2,2,2,2]]
```

**Constraints**
* `1 <= nums.length <= 200`; `-10^9 <= nums[i], target <= 10^9`

## Approach: Sort + two loops + two pointers

> Fix two numbers with nested loops (skipping duplicates), then find the remaining pair with two pointers.

**Extend 3Sum.** Sort. Loop `i`, then `j > i` (skipping equal neighbours), then two pointers on the rest. Sums use `long`, since four
values near 10⁹ overflow an `int`.

* Time: **O(n³)** — n² pairs × a linear scan.
* Space: **O(log n)** — sorting (plus the output).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0018/v1/FourSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0018/v1/FourSumTest.java` | JUnit 6 tests |
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
