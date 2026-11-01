# 274. H-Index — v1: Sort descending

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/h-index/)

## Problem

`citations[i]` is the number of citations of a researcher's `i`-th paper. Return the researcher's **h-index**: the largest
`h` such that at least `h` papers each have at least `h` citations.

**Example 1**
```
Input:  citations = [3,0,6,1,5]
Output: 3   (three papers have ≥ 3 citations)
```

**Example 2**
```
Input:  citations = [1,3,1]
Output: 1
```

**Constraints**
* `1 <= n <= 5000`
* `0 <= citations[i] <= 1000`

## Approach: Sort descending

> Sort citations high to low; h grows while the (h+1)-th paper still has more than h citations.

**Sort.** Sort ascending and scan from the top: the paper at rank `h + 1` (counting from the most cited) must have at least
`h + 1` citations for the h-index to reach `h + 1`.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0274/v1/HIndex.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0274/v1/HIndexTest.java` | JUnit 6 tests |
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

* [v2-counting-buckets](../v2-counting-buckets/README.md): Counting buckets (`O(n)` time, `O(n)` space)
