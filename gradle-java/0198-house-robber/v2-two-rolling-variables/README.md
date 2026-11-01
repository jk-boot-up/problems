# 198. House Robber — v2: Two rolling variables

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/house-robber/)

## Problem

Houses along a street hold `nums[i]` money. You cannot rob two **adjacent** houses. Return the maximum amount you can rob.

**Example**
```
[1,2,3,1] → 4 (1 + 3),   [2,7,9,3,1] → 12 (2 + 9 + 1)
```

**Constraints**
* `1 <= nums.length <= 100`; `0 <= nums[i] <= 400`

## Approach: Two rolling variables

> At each house: either rob it (plus the best up to two houses back) or skip it (keep the best up to the previous house).

**DP.** `best(i) = max(best(i-1), best(i-2) + nums[i])`. Keep only `prev2` and `prev1`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two variables.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0198/v2/HouseRobber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0198/v2/HouseRobberTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-dp-table](../v1-dp-table/README.md): DP table (`O(n)` time, `O(n)` space)
