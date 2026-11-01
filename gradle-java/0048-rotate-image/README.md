# 48. Rotate Image

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rotate-image/)

## Problem

Rotate an `n × n` matrix by 90 degrees **clockwise**, **in place** (do not allocate another matrix).

**Example 1**
```
Input:  [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2**
```
Input:  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**Constraints**
* `1 <= n <= 20`, `-1000 <= matrix[i][j] <= 1000`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-copy-into-a-new-matrix](v1-copy-into-a-new-matrix/README.md) | Copy into a new matrix | `O(n²)` | `O(n²)` | [▶ animation](v1-copy-into-a-new-matrix/animation/index.html) |
| [v2-transpose-reverse-rows](v2-transpose-reverse-rows/README.md) | Transpose + reverse rows | `O(n²)` | `O(1)` | [▶ animation](v2-transpose-reverse-rows/animation/index.html) |
