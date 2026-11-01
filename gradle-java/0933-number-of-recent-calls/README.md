# 933. Number of Recent Calls

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Queue &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-recent-calls/)

## Problem

Implement `RecentCounter` with `ping(t)`: record a request at time `t` (strictly increasing) and return how many requests happened in the
inclusive range `[t - 3000, t]`.

**Example**
```
ping(1) → 1, ping(100) → 2, ping(3001) → 3, ping(3002) → 3
```

**Constraints**
* `1 <= t <= 10^9`; at most `10^4` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sliding-queue](v1-sliding-queue/README.md) | Sliding queue | `O(1)` | `O(W)` | [▶ animation](v1-sliding-queue/animation/index.html) |
