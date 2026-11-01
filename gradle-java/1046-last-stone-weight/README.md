# 1046. Last Stone Weight

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/last-stone-weight/)

## Problem

Repeatedly smash the two heaviest stones `x <= y`: if equal, both vanish; otherwise a stone of weight `y - x` remains. Return the weight of
the last stone, or 0 if none remain.

**Example**
```
[2,7,4,1,8,1] → 1
```

**Constraints**
* `1 <= stones.length <= 30`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-max-heap-simulation](v1-max-heap-simulation/README.md) | Max-heap simulation | `O(n log n)` | `O(n)` | [▶ animation](v1-max-heap-simulation/animation/index.html) |
