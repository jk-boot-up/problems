# 274. H-Index

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

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Sort descending | `O(n log n)` | `O(log n)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Counting buckets | `O(n)` | `O(n)` | [▶ animation](v2/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
