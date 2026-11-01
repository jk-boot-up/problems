# 621. Task Scheduler

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/task-scheduler/)

## Problem

CPU tasks are letters; each takes one interval. The same task must be separated by at least `n` intervals (idle intervals allowed).
Return the minimum number of intervals to finish all tasks.

**Example**
```
tasks = [A,A,A,B,B,B], n = 2 → 8   (A B idle A B idle A B)
tasks = [A,C,A,B,D,B], n = 1 → 6
```

**Constraints**
* `1 <= tasks.length <= 10^4`; `0 <= n <= 100`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-simulation-with-a-max-heap](v1-greedy-simulation-with-a-max-heap/README.md) | Greedy simulation with a max-heap | `O(N log 26)` | `O(1)` | [▶ animation](v1-greedy-simulation-with-a-max-heap/animation/index.html) |
| [v2-counting-formula](v2-counting-formula/README.md) | Counting formula | `O(N)` | `O(1)` | [▶ animation](v2-counting-formula/animation/index.html) |
