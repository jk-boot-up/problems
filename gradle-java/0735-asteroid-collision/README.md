# 735. Asteroid Collision

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/asteroid-collision/)

## Problem

Each asteroid's size is `|a|` and its direction is its sign (`+` right, `-` left); all move at the same speed. When two meet, the smaller
explodes; equal sizes both explode. Return the asteroids left after all collisions.

**Example**
```
[5,10,-5] → [5,10],   [8,-8] → [],   [10,2,-5] → [10],   [-2,-1,1,2] → [-2,-1,1,2]
```

**Constraints**
* `2 <= n <= 10^4`; `a != 0`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-stack-of-survivors](v1-stack-of-survivors/README.md) | Stack of survivors | `O(n)` | `O(n)` | [▶ animation](v1-stack-of-survivors/animation/index.html) |
