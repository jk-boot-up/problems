# 1291. Sequential Digits

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Enumeration &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sequential-digits/)

## Problem

A number has **sequential digits** if each digit is one more than the previous (like `1234`). Return all such numbers in `[low, high]`,
sorted.

**Example**
```
low = 100,  high = 300   → [123,234]
low = 1000, high = 13000 → [1234,2345,3456,4567,5678,6789,12345]
```

**Constraints**
* `10 <= low <= high <= 10^9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-enumerate-by-length-and-start](v1-enumerate-by-length-and-start/README.md) | Enumerate by length and start | `O(1)` | `O(1)` | [▶ animation](v1-enumerate-by-length-and-start/animation/index.html) |
