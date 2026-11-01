# 739. Daily Temperatures

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/daily-temperatures/)

## Problem

For each day, return how many days you must wait for a **warmer** temperature (0 if none).

**Example**
```
[73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
```

**Constraints**
* `1 <= n <= 10^5`; `30 <= temperatures[i] <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-monotonic-stack](v1-monotonic-stack/README.md) | Monotonic stack | `O(n)` | `O(n)` | [▶ animation](v1-monotonic-stack/animation/index.html) |
