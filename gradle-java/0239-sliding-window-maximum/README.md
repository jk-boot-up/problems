# 239. Sliding Window Maximum

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sliding-window-maximum/)

## Problem

A window of size `k` slides over `nums` from left to right. Return the maximum of each window position.

**Example**
```
nums = [1,3,-1,-3,5,3,6,7], k = 3 → [3,3,5,5,6,7]
```

**Constraints**
* `1 <= k <= nums.length <= 10^5`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-monotonic-deque](v1-monotonic-deque/README.md) | Monotonic deque | `O(n)` | `O(k)` | [▶ animation](v1-monotonic-deque/animation/index.html) |
