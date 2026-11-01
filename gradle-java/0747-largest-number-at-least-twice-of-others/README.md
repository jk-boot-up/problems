# 747. Largest Number At Least Twice of Others

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/largest-number-at-least-twice-of-others/)

## Problem

The largest value in `nums` is unique. Return its index if it is at least twice every other value, otherwise `-1`.

**Example**
```
[3,6,1,0] → 1,   [1,2,3,4] → -1
```

**Constraints**
* `2 <= nums.length <= 50`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-track-the-top-two](v1-track-the-top-two/README.md) | Track the top two | `O(n)` | `O(1)` | [▶ animation](v1-track-the-top-two/animation/index.html) |
