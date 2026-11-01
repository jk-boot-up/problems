# 210. Course Schedule II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/course-schedule-ii/)

## Problem

Same setup as Course Schedule: `prerequisites[i] = [a, b]` means `b` before `a`. Return **an ordering** of all courses that respects
every prerequisite, or an empty array if impossible. Any valid order is accepted.

**Example 1**
```
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
```

**Example 2**
```
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
```

**Constraints**
* `1 <= numCourses <= 2000`; pairs are unique.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-kahn-s-topological-sort](v1-kahn-s-topological-sort/README.md) | Kahn's topological sort | `O(V + E)` | `O(V + E)` | [▶ animation](v1-kahn-s-topological-sort/animation/index.html) |
