# 451. Sort Characters By Frequency

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sorting &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sort-characters-by-frequency/)

## Problem

Sort a string so that characters appearing more often come first; equal characters stay together. Among characters with the same count,
this project lists them in character-code order.

**Example**
```
"tree"   → "eert"
"cccaaa" → "aaaccc"
"Aabb"   → "bbAa"
```

**Constraints**
* `1 <= s.length <= 5 * 10^5`; letters and digits

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bucket-sort-by-count](v1-bucket-sort-by-count/README.md) | Bucket sort by count | `O(n)` | `O(n)` | [▶ animation](v1-bucket-sort-by-count/animation/index.html) |
