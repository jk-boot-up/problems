# 137. Single Number II

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/single-number-ii/)

## Problem

Every element appears **three times** except one, which appears exactly once. Find it in linear time and constant extra space.

**Example**
```
[2,2,3,2] → 3,   [0,1,0,1,0,1,99] → 99
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-count-each-bit-position](v1-count-each-bit-position/README.md) | Count each bit position | `O(32·n)` | `O(1)` | [▶ animation](v1-count-each-bit-position/animation/index.html) |
| [v2-ones-twos-bit-counters](v2-ones-twos-bit-counters/README.md) | Ones/twos bit counters | `O(n)` | `O(1)` | [▶ animation](v2-ones-twos-bit-counters/animation/index.html) |
