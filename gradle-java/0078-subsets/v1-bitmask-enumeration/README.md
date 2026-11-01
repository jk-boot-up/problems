# 78. Subsets — v1: Bitmask enumeration

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subsets/)

## Problem

Given an array of **unique** integers, return all possible subsets (the power set), in any order, without duplicates.

**Example**
```
[1,2,3] → [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Constraints**
* `1 <= nums.length <= 10`

## Approach: Bitmask enumeration

> Each number from 0 to 2ⁿ − 1 is a bitmask choosing a subset.

**Bitmasks.** For `mask` in `0 .. 2ⁿ - 1`, include `nums[i]` when bit `i` is set.

* Time: **O(n · 2ⁿ)** — 2ⁿ masks, n bits each.
* Space: **O(n)** — one subset at a time (plus the output).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0078/v1/Subsets.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0078/v1/SubsetsTest.java` | JUnit 6 tests |
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

* [v2-backtracking](../v2-backtracking/README.md): Backtracking (`O(n · 2ⁿ)` time, `O(n)` space)
