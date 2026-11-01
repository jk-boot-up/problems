# 724. Find Pivot Index — v1: Total minus running left sum

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-pivot-index/)

## Problem

Return the leftmost index where the sum of the elements to its left equals the sum of the elements to its right (an empty side sums to 0),
or `-1`.

**Example**
```
[1,7,3,6,5,6] → 3,   [1,2,3] → -1,   [2,1,-1] → 0
```

**Constraints**
* `1 <= nums.length <= 10^4`

## Approach: Total minus running left sum

> The pivot is where the sum to its left equals total − left − nums[i].

**One total, one running sum.** The right side's sum is `total - left - nums[i]`; check it equals `left`, then add `nums[i]` to `left`.

* Time: **O(n)** — two passes.
* Space: **O(1)** — two sums.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0724/v1/FindPivotIndex.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0724/v1/FindPivotIndexTest.java` | JUnit 6 tests |
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
