# 315. Count of Smaller Numbers After Self — v1: Brute force

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Divide and Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

## Problem

For each `nums[i]`, count how many elements to its **right** are strictly smaller. Return the counts.

**Example**
```
[5,2,6,1] → [2,1,1,0]
[-1]      → [0]
[-1,-1]   → [0,0]
```

**Constraints**
* `1 <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`

## Approach: Brute force

> For every element, scan everything to its right.

**Double loop.** Count `nums[j] < nums[i]` for each `j > i`.

* Time: **O(n²)** — every pair.
* Space: **O(1)** — besides the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0315/v1/CountSmaller.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0315/v1/CountSmallerTest.java` | JUnit 6 tests |
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

* [v2-merge-sort-counting-inversions](../v2-merge-sort-counting-inversions/README.md): Merge sort counting inversions (`O(n log n)` time, `O(n)` space)
