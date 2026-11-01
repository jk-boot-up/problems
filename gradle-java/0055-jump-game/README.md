# 55. Jump Game

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/jump-game/)

## Problem

You start at index `0` of `nums`. Each `nums[i]` is the **maximum** jump length from position `i`.
Return `true` if you can reach the last index, otherwise `false`.

**Example 1**
```
Input:  nums = [2,3,1,1,4]
Output: true   (0 → 1 → 4)
```

**Example 2**
```
Input:  nums = [3,2,1,0,4]
Output: false  (every path gets stuck at index 3)
```

**Constraints**
* `1 <= nums.length <= 10^4`
* `0 <= nums[i] <= 10^5`

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(n)` | `O(1)` | [▶ animation](v1/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
