# 312. Burst Balloons — v1: Interval DP on the last balloon

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/burst-balloons/)

## Problem

Bursting balloon `i` earns `nums[left] * nums[i] * nums[right]`, where `left` and `right` are its current neighbours (out of range counts
as 1). Burst all balloons to collect the maximum total.

**Example**
```
[3,1,5,8] → 167   (3·1·5 + 3·5·8 + 1·3·8 + 1·8·1)
[1,5]     → 10
```

**Constraints**
* `1 <= n <= 300`; `0 <= nums[i] <= 100`

## Approach: Interval DP on the last balloon

> Think about the LAST balloon burst in an interval: its neighbours are then the interval's fixed boundaries.

**Interval DP.** Pad with 1s: `a = [1, nums…, 1]`. `dp[l][r]` = best coins from bursting everything strictly between `l` and `r`. If `k`
is the last one burst there, its neighbours are `a[l]` and `a[r]`: `dp[l][r] = max(dp[l][k] + a[l]·a[k]·a[r] + dp[k][r])`. Fill by
increasing gap.

* Time: **O(n³)** — n² intervals × n choices of k.
* Space: **O(n²)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0312/v1/BurstBalloons.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0312/v1/BurstBalloonsTest.java` | JUnit 6 tests |
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
