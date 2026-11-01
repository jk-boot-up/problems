# 47. Permutations II — v1: Sorted backtracking with used flags

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/permutations-ii/)

## Problem

`nums` may contain duplicates. Return all **unique** permutations, in any order.

**Example**
```
[1,1,2] → [[1,1,2],[1,2,1],[2,1,1]]
```

**Constraints**
* `1 <= nums.length <= 8`

## Approach: Sorted backtracking with used flags

> Sort, and only use a duplicate value when its earlier twin is already in the path, so equal values keep a fixed order.

**Order equal values.** Sort. Skip `nums[i]` if it is used, or if `nums[i] == nums[i-1]` and `nums[i-1]` is **not** used: that forces
equal values to be placed left to right, so each distinct arrangement appears once.

* Time: **O(n · n!)** — at most n! permutations, each copied in O(n).
* Space: **O(n)** — flags and recursion.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0047/v1/PermutationsII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0047/v1/PermutationsIITest.java` | JUnit 6 tests |
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
