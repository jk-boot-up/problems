# 72. Edit Distance

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/edit-distance/)

## Problem

Return the minimum number of operations (insert a character, delete a character, replace a character) to convert `word1` into `word2`.

**Example**
```
horse → ros:  3  (replace h→r, delete r, delete e)
intention → execution:  5
```

**Constraints**
* `0 <= word1.length, word2.length <= 500`; lowercase letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-2d-dp-table](v1-2d-dp-table/README.md) | 2D DP table | `O(m·n)` | `O(m·n)` | [▶ animation](v1-2d-dp-table/animation/index.html) |
