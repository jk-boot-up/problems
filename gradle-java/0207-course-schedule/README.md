# 207. Course Schedule

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/course-schedule/)

## Problem

There are `numCourses` courses `0..numCourses-1`. `prerequisites[i] = [a, b]` means you must take `b` before `a`. Return `true` if
it is possible to finish all courses.

**Example 1**
```
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: true
```

**Example 2**
```
Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false   (a cycle)
```

**Constraints**
* `1 <= numCourses <= 2000`; `0 <= prerequisites.length <= 5000`; pairs are unique.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dfs-cycle-detection](v1-dfs-cycle-detection/README.md) | DFS cycle detection | `O(V + E)` | `O(V + E)` | [▶ animation](v1-dfs-cycle-detection/animation/index.html) |
| [v2-kahn-s-topological-sort](v2-kahn-s-topological-sort/README.md) | Kahn's topological sort | `O(V + E)` | `O(V + E)` | [▶ animation](v2-kahn-s-topological-sort/animation/index.html) |
