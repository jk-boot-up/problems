# 45. Jump Game II — v2: Greedy windows

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

## Approach: Greedy windows

> Breadth-first in disguise: each jump covers a window of indices; the next window ends at the farthest reach from it.

**Greedy levels.** All indices reachable with `j` jumps form a window ending at `end`. While scanning that window, track
`farthest = max(i + nums[i])`. When `i` reaches `end`, we must take another jump: `jumps++`, `end = farthest`.

* Time: **O(n)** — every index is scanned once across all windows.
* Space: **O(1)** — three counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0045/v2/JumpGameII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0045/v2/JumpGameIITest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-dynamic-programming](../v1-dynamic-programming/README.md): Dynamic programming (`O(n²)` time, `O(n)` space)
