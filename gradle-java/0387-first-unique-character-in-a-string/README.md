# 387. First Unique Character in a String

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/)

## Problem

Return the index of the first character of `s` that does not repeat, or `-1`.

**Example**
```
"leetcode" → 0,   "loveleetcode" → 2,   "aabb" → -1
```

**Constraints**
* `1 <= s.length <= 10^5`; lowercase letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-counting-array](v1-counting-array/README.md) | Counting array | `O(n)` | `O(1)` | [▶ animation](v1-counting-array/animation/index.html) |
