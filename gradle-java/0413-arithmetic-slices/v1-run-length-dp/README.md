# 413. Arithmetic Slices — v1: Run length DP

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/arithmetic-slices/)

## Problem

An array is **arithmetic** if it has at least three elements and equal differences between neighbours. Return the number of arithmetic
contiguous subarrays of `nums`.

**Example**
```
[1,2,3,4] → 3   ([1,2,3], [2,3,4], [1,2,3,4])
[1]       → 0
```

**Constraints**
* `1 <= nums.length <= 5000`

## Approach: Run length DP

> If the slice ending at i − 1 extends to i, every one of those slices grows by one, plus one new 3-element slice.

**Count slices ending here.** Let `cur` be the number of arithmetic slices ending at `i`. If `nums[i] - nums[i-1] == nums[i-1] - nums[i-2]`,
then `cur = previous cur + 1` (all earlier slices extend, plus the new three-element one); otherwise `cur = 0`. Sum `cur` over all `i`.

* Time: **O(n)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0413/v1/ArithmeticSlices.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0413/v1/ArithmeticSlicesTest.java` | JUnit 6 tests |
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
