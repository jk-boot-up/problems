# 846. Hand of Straights

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/hand-of-straights/)

## Problem

Can the cards in `hand` be rearranged into groups of `groupSize` **consecutive** values?

**Example**
```
hand = [1,2,3,6,2,3,4,7,8], groupSize = 3 → true ([1,2,3],[2,3,4],[6,7,8])
hand = [1,2,3,4,5], groupSize = 4          → false
```

**Constraints**
* `1 <= hand.length <= 10^4`; `1 <= groupSize <= hand.length`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-counts](v1-sort-counts/README.md) | Sort + counts | `O(n log n)` | `O(n)` | [▶ animation](v1-sort-counts/animation/index.html) |
