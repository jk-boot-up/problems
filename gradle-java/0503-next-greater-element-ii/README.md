# 503. Next Greater Element II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/next-greater-element-ii/)

## Problem

`nums` is **circular**. For each element, return the first greater value found by moving right (wrapping around), or `-1`.

**Example**
```
[1,2,1] → [2,-1,2],   [1,2,3,4,3] → [2,3,4,-1,4]
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-monotonic-stack-over-two-passes](v1-monotonic-stack-over-two-passes/README.md) | Monotonic stack over two passes | `O(n)` | `O(n)` | [▶ animation](v1-monotonic-stack-over-two-passes/animation/index.html) |
