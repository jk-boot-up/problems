# 1207. Unique Number of Occurrences

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-number-of-occurrences/)

## Problem

Return `true` if the number of occurrences of each value in `arr` is unique.

**Example**
```
[1,2,2,1,1,3] → true (counts 3, 2, 1),   [1,2] → false
```

**Constraints**
* `1 <= arr.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-counts-set-of-counts](v1-counts-set-of-counts/README.md) | Counts + set of counts | `O(n)` | `O(n)` | [▶ animation](v1-counts-set-of-counts/animation/index.html) |
