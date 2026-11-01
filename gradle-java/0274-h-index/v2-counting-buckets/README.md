# 274. H-Index — v2: Counting buckets

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

## Approach: Counting buckets

> Count papers by citation (capped at n), then walk down from n until at least h papers have h or more citations.

**Counting sort.** The answer is at most `n`, so put every paper into a bucket `min(c, n)`. Walk `h` from `n` down to 0,
keeping a running total of papers with at least `h` citations. The first `h` where that total reaches `h` is the answer.

* Time: **O(n)** — one pass to fill buckets, one pass down them.
* Space: **O(n)** — the bucket array of size n + 1.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0274/v2/HIndex.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0274/v2/HIndexTest.java` | JUnit 6 tests |
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

* [v1-sort-descending](../v1-sort-descending/README.md): Sort descending (`O(n log n)` time, `O(log n)` space)
