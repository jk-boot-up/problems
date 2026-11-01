# 1376. Time Needed to Inform All Employees

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/time-needed-to-inform-all-employees/)

## Problem

A company has `n` employees; `manager[i]` is the direct manager of `i` (`-1` for the head, `headID`). Starting with the head, each manager
needs `informTime[i]` minutes to tell all direct reports, who then pass it on. Return the minutes until everyone knows.

**Example**
```
n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0] → 1
n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1] → 21
```

**Constraints**
* `1 <= n <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-down-the-management-tree](v1-bfs-down-the-management-tree/README.md) | BFS down the management tree | `O(n)` | `O(n)` | [▶ animation](v1-bfs-down-the-management-tree/animation/index.html) |
