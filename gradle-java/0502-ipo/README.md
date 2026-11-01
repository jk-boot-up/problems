# 502. IPO

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ipo/)

## Problem

You have initial capital `w` and may finish at most `k` distinct projects. Project `i` needs at least `capital[i]` to start and adds
`profits[i]` to your capital when finished. Return the maximum capital after at most `k` projects.

**Example**
```
Input:  k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4   (do project 0 → w = 1, then project 2 → w = 4)
```

**Constraints**
* `1 <= k <= 10^5`; `0 <= w <= 10^9`; `1 <= n <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-by-capital-max-heap-of-profits](v1-sort-by-capital-max-heap-of-profits/README.md) | Sort by capital + max-heap of profits | `O(n log n)` | `O(n)` | [▶ animation](v1-sort-by-capital-max-heap-of-profits/animation/index.html) |
