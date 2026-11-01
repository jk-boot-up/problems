# 1029. Two City Scheduling

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/two-city-scheduling/)

## Problem

`2n` people are interviewing; `costs[i] = [aCost, bCost]` is the cost of flying person `i` to city A or B. Exactly `n` people must go to
each city. Return the minimum total cost.

**Example**
```
[[10,20],[30,200],[400,50],[30,20]] → 110   (A: 10, 30; B: 50, 20)
```

**Constraints**
* `2 <= costs.length <= 100`, even

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-by-cost-difference](v1-sort-by-cost-difference/README.md) | Sort by cost difference | `O(n log n)` | `O(n)` | [▶ animation](v1-sort-by-cost-difference/animation/index.html) |
