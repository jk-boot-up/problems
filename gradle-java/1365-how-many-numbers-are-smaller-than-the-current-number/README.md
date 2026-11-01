# 1365. How Many Numbers Are Smaller Than the Current Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)

## Problem

For each `nums[i]`, return how many other values in `nums` are strictly smaller.

**Example**
```
[8,1,2,2,3] → [4,0,1,1,3],   [6,5,4,8] → [2,1,0,3],   [7,7,7,7] → [0,0,0,0]
```

**Constraints**
* `2 <= nums.length <= 500`; `0 <= nums[i] <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-counting-sort-prefix-sums](v1-counting-sort-prefix-sums/README.md) | Counting sort prefix sums | `O(n + R)` | `O(R)` | [▶ animation](v1-counting-sort-prefix-sums/animation/index.html) |
