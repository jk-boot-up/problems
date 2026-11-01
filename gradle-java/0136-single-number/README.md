# 136. Single Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/single-number/)

## Problem

Every element of a non-empty array appears **twice** except one. Find that one, in linear time and constant extra space.

**Example**
```
[2,2,1] → 1,   [4,1,2,1,2] → 4,   [1] → 1
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-set-toggling](v1-hash-set-toggling/README.md) | Hash set toggling | `O(n)` | `O(n)` | [▶ animation](v1-hash-set-toggling/animation/index.html) |
| [v2-xor-everything](v2-xor-everything/README.md) | XOR everything | `O(n)` | `O(1)` | [▶ animation](v2-xor-everything/animation/index.html) |
