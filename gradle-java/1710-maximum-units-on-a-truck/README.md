# 1710. Maximum Units on a Truck

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-units-on-a-truck/)

## Problem

`boxTypes[i] = [count, unitsPerBox]`. A truck holds at most `truckSize` boxes. Return the maximum total units it can carry.

**Example**
```
boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4 → 8
boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10 → 91
```

**Constraints**
* `1 <= boxTypes.length <= 1000`, `1 <= count, unitsPerBox <= 1000`, `1 <= truckSize <= 10^6`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-by-units-per-box](v1-greedy-by-units-per-box/README.md) | Greedy by units per box | `O(n + U)` | `O(U)` | [▶ animation](v1-greedy-by-units-per-box/animation/index.html) |
