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

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-descending](v1-sort-descending/README.md) | Sort descending | `O(n log n)` | `O(log n)` | [▶ animation](v1-sort-descending/animation/index.html) |
| [v2-counting-buckets](v2-counting-buckets/README.md) | Counting buckets | `O(n)` | `O(n)` | [▶ animation](v2-counting-buckets/animation/index.html) |
