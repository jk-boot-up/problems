# 2462. Total Cost to Hire K Workers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/total-cost-to-hire-k-workers/)

## Problem

Hire exactly `k` workers in `k` sessions. In each session, choose the cheapest worker among the first `candidates` and the last `candidates`
remaining workers (ties go to the smaller index). Return the total cost.

**Example**
```
costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4 → 11
costs = [1,2,4,1], k = 3, candidates = 3               → 4
```

**Constraints**
* `1 <= k, candidates <= costs.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-heaps-from-both-ends](v1-two-heaps-from-both-ends/README.md) | Two heaps from both ends | `O((k + candidates) log candidates)` | `O(candidates)` | [▶ animation](v1-two-heaps-from-both-ends/animation/index.html) |
