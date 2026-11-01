# 45. Jump Game II — v1: Dynamic programming

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/jump-game-ii/)

## Problem

You start at index `0` of `nums`; `nums[i]` is the maximum jump length from `i`. The last index is always reachable.
Return the **minimum number of jumps** needed to reach the last index.

**Example 1**
```
Input:  nums = [2,3,1,1,4]
Output: 2   (0 → 1 → 4)
```

**Example 2**
```
Input:  nums = [2,3,0,1,4]
Output: 2
```

**Constraints**
* `1 <= nums.length <= 10^4`
* `0 <= nums[i] <= 1000`
* The last index is reachable.

## Approach: Dynamic programming

> jumps[i] = fewest jumps to reach i; relax every index reachable from i.

**DP over positions.** `dp[0] = 0`, every other entry starts at infinity. For each `i`, for each `j` in `i+1 … i+nums[i]`,
set `dp[j] = min(dp[j], dp[i] + 1)`.

* Time: **O(n²)** — each index may relax up to n later indices.
* Space: **O(n)** — the dp array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0045/v1/JumpGameII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0045/v1/JumpGameIITest.java` | JUnit 6 tests |
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

* [v2-greedy-windows](../v2-greedy-windows/README.md): Greedy windows (`O(n)` time, `O(1)` space)
