# 287. Find the Duplicate Number

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/)

## Problem

`nums` has `n + 1` integers, each in `[1, n]`. Exactly one value is repeated (possibly many times). Return it without modifying the
array and using O(1) extra space.

**Example**
```
[1,3,4,2,2] → 2,   [3,1,3,4,2] → 3,   [3,3,3,3,3] → 3
```

**Constraints**
* `1 <= n <= 10^5`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-seen-set](v1-seen-set/README.md) | Seen set | `O(n)` | `O(n)` | [▶ animation](v1-seen-set/animation/index.html) |
| [v2-floyd-cycle-detection](v2-floyd-cycle-detection/README.md) | Floyd cycle detection | `O(n)` | `O(1)` | [▶ animation](v2-floyd-cycle-detection/animation/index.html) |
