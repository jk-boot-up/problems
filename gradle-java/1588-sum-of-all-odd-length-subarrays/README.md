# 1588. Sum of All Odd Length Subarrays

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)

## Problem

Return the sum of all elements of all **odd-length** subarrays of `arr`.

**Example**
```
[1,4,2,5,3] → 58
[1,2]       → 3
[10,11,12]  → 66
```

**Constraints**
* `1 <= arr.length <= 100`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-prefix-sums-over-every-odd-length](v1-prefix-sums-over-every-odd-length/README.md) | Prefix sums over every odd length | `O(n²)` | `O(n)` | [▶ animation](v1-prefix-sums-over-every-odd-length/animation/index.html) |
| [v2-contribution-counting](v2-contribution-counting/README.md) | Contribution counting | `O(n)` | `O(1)` | [▶ animation](v2-contribution-counting/animation/index.html) |
