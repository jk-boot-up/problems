# 217. Contains Duplicate

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contains-duplicate/)

## Problem

Return `true` if any value appears **at least twice** in `nums`, and `false` if every element is distinct.

**Example**
```
[1,2,3,1] → true,   [1,2,3,4] → false,   [1,1,1,3,3,4,3,2,4,2] → true
```

**Constraints**
* `1 <= nums.length <= 10^5`; `-10^9 <= nums[i] <= 10^9`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-and-compare-neighbours](v1-sort-and-compare-neighbours/README.md) | Sort and compare neighbours | `O(n log n)` | `O(n)` | [▶ animation](v1-sort-and-compare-neighbours/animation/index.html) |
| [v2-hash-set](v2-hash-set/README.md) | Hash set | `O(n)` | `O(n)` | [▶ animation](v2-hash-set/animation/index.html) |
