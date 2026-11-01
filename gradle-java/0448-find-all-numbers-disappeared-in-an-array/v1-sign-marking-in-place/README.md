# 448. Find All Numbers Disappeared in an Array — v1: Sign marking in place

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

## Problem

`nums` has `n` values in `[1, n]`. Return every number in `[1, n]` that does not appear.

**Example**
```
[4,3,2,7,8,2,3,1] → [5,6],   [1,1] → [2]
```

**Constraints**
* `1 <= n <= 10^5`

**Follow-up:** no extra space (the output does not count).

## Approach: Sign marking in place

> Mark value v as seen by making nums[v−1] negative; indices left positive are the missing numbers.

**Signs as flags.** For each value `v = |nums[i]|`, make `nums[v-1]` negative. Afterwards, index `i` still positive means `i + 1` never
appeared. (We work on a copy so the input is untouched.)

* Time: **O(n)** — two passes.
* Space: **O(1)** — apart from the copy and output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0448/v1/FindDisappearedNumbers.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0448/v1/FindDisappearedNumbersTest.java` | JUnit 6 tests |
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
