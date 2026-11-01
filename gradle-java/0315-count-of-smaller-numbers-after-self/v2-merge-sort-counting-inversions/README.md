# 315. Count of Smaller Numbers After Self — v2: Merge sort counting inversions

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

## Approach: Merge sort counting inversions

> During merge sort, every right-half element that is placed before a left-half element is smaller and lies after it.

**Merge sort on indices.** Sort an index array by value. When merging two sorted halves, an element taken from the left half has
exactly `j - (mid + 1)` right-half elements already placed before it, and those are smaller (ties go left first, so only strictly
smaller ones count) and originally to its right. Add that to its count.

* Time: **O(n log n)** — merge sort.
* Space: **O(n)** — the index and buffer arrays.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0315/v2/CountSmaller.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0315/v2/CountSmallerTest.java` | JUnit 6 tests |
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

* [v1-brute-force](../v1-brute-force/README.md): Brute force (`O(n²)` time, `O(1)` space)
