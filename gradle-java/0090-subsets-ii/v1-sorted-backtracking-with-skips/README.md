# 90. Subsets II — v1: Sorted backtracking with skips

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subsets-ii/)

## Problem

`nums` may contain duplicates. Return all **distinct** subsets, in any order.

**Example**
```
[1,2,2] → [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**Constraints**
* `1 <= nums.length <= 10`

## Approach: Sorted backtracking with skips

> Sort, then at each depth skip a value equal to the previous one tried at that same depth.

**Skip duplicate branches.** Sort. In the loop at a given depth, skip `i > start` with `nums[i] == nums[i-1]`: that choice would
start a branch identical to the one just explored.

* Time: **O(n · 2ⁿ)** — at most 2ⁿ subsets, each copied in O(n).
* Space: **O(n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0090/v1/SubsetsII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0090/v1/SubsetsIITest.java` | JUnit 6 tests |
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
