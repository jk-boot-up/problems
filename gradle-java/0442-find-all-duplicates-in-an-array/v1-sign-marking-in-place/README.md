# 442. Find All Duplicates in an Array — v1: Sign marking in place

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

## Problem

`nums` has `n` values in `[1, n]`, each appearing once or twice. Return all values that appear twice, in O(n) time and O(1) extra space.

**Example**
```
[4,3,2,7,8,2,3,1] → [2,3],   [1,1,2] → [1],   [1] → []
```

**Constraints**
* `1 <= n <= 10^5`

## Approach: Sign marking in place

> Flip the sign at index v−1 when you see v; finding it already negative means v is a duplicate.

**Signs as flags.** For each `v = |nums[i]|`: if `nums[v-1]` is already negative, `v` has been seen: record it; otherwise negate it.

* Time: **O(n)** — one pass.
* Space: **O(1)** — apart from the copy and output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0442/v1/FindAllDuplicates.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0442/v1/FindAllDuplicatesTest.java` | JUnit 6 tests |
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
