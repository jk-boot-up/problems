# 55. Jump Game — v1: Greedy reach

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

## Approach: Greedy reach

> Track the farthest index reachable so far; if you ever stand beyond it, you are stuck.

**Greedy reach.** Keep `reach`, the farthest index reachable so far. Walk `i` left to right. If `i > reach` you can't get here,
so return `false`. Otherwise update `reach = max(reach, i + nums[i])`. Return `true` once `reach` covers the last index.

* Time: **O(n)** — each index is visited at most once.
* Space: **O(1)** — a single reach variable.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0055/v1/JumpGame.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0055/v1/JumpGameTest.java` | JUnit 6 tests |
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
