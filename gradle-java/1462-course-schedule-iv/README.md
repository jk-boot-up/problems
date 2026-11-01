# 1462. Course Schedule IV

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/course-schedule-iv/)

## Problem

There are `numCourses` courses. `prerequisites[i] = [a, b]` means `a` must be taken before `b`. Prerequisites are transitive. For each
query `[u, v]`, return whether `u` is a (direct or indirect) prerequisite of `v`.

**Example**
```
numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]] → [false,true]
numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]] → [true,true]
```

**Constraints**
* `2 <= numCourses <= 100`, no cycles, up to `10^4` queries

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-transitive-closure](v1-transitive-closure/README.md) | Transitive closure | `O(n³ + q)` | `O(n²)` | [▶ animation](v1-transitive-closure/animation/index.html) |
