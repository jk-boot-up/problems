# 628. Maximum Product of Three Numbers — v1: Track top three and bottom two

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/)

## Problem

Return the maximum product of three numbers in `nums`.

**Example**
```
[1,2,3] → 6,   [1,2,3,4] → 24,   [-1,-2,-3] → -6,   [-10,-10,1,3,2] → 300
```

**Constraints**
* `3 <= nums.length <= 10^4`; `-1000 <= nums[i] <= 1000`

## Approach: Track top three and bottom two

> The best product is either the three largest values or the two smallest (most negative) times the largest.

**One pass.** Keep the three largest and two smallest values. Answer `max(max1·max2·max3, min1·min2·max1)`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — five numbers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0628/v1/MaximumProductOfThree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0628/v1/MaximumProductOfThreeTest.java` | JUnit 6 tests |
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
