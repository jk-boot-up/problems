# 771. Jewels and Stones

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/jewels-and-stones/)

## Problem

`jewels` lists the letter types that are jewels; `stones` lists your stones. Return how many of your stones are jewels (case-sensitive).

**Example**
```
jewels = "aA", stones = "aAAbbbb" → 3,   jewels = "z", stones = "ZZ" → 0
```

**Constraints**
* `1 <= jewels.length, stones.length <= 50`; letters only.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-lookup-table](v1-lookup-table/README.md) | Lookup table | `O(j + s)` | `O(1)` | [▶ animation](v1-lookup-table/animation/index.html) |
