# 1299. Replace Elements with Greatest Element on Right Side

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)

## Problem

Replace every element with the greatest element to its right, and the last element with `-1`.

**Example**
```
[17,18,5,4,6,1] → [18,6,6,6,1,-1],   [400] → [-1]
```

**Constraints**
* `1 <= arr.length <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-right-to-left-running-maximum](v1-right-to-left-running-maximum/README.md) | Right-to-left running maximum | `O(n)` | `O(1)` | [▶ animation](v1-right-to-left-running-maximum/animation/index.html) |
