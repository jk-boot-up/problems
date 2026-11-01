# 134. Gas Station

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/gas-station/)

## Problem

There are `n` gas stations on a circular route. Station `i` gives `gas[i]` fuel, and driving from station `i` to `i + 1`
costs `cost[i]`. Starting with an empty tank, return the index of the station from which you can drive all the way around
once, or `-1` if impossible. If a solution exists it is unique.

**Example 1**
```
Input:  gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
```

**Example 2**
```
Input:  gas = [2,3,4], cost = [3,4,3]
Output: -1
```

**Constraints**
* `1 <= n <= 10^5`
* `0 <= gas[i], cost[i] <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-simulate-every-start](v1-simulate-every-start/README.md) | Simulate every start | `O(n²)` | `O(1)` | [▶ animation](v1-simulate-every-start/animation/index.html) |
| [v2-greedy-single-pass](v2-greedy-single-pass/README.md) | Greedy single pass | `O(n)` | `O(1)` | [▶ animation](v2-greedy-single-pass/animation/index.html) |
