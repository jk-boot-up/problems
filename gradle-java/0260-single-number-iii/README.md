# 260. Single Number III

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/single-number-iii/)

## Problem

In `nums`, exactly two elements appear once and every other element appears exactly twice. Return the two single elements, in any order,
using O(1) extra space.

**Example**
```
[1,2,1,3,2,5] → [3,5]
[-1,0]        → [-1,0]
```

**Constraints**
* `2 <= nums.length <= 3 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-xor-and-split-by-a-differing-bit](v1-xor-and-split-by-a-differing-bit/README.md) | XOR and split by a differing bit | `O(n)` | `O(1)` | [▶ animation](v1-xor-and-split-by-a-differing-bit/animation/index.html) |
