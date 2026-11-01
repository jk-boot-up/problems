# 581. Shortest Unsorted Continuous Subarray

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)

## Problem

Find the shortest contiguous subarray that, if sorted, makes the whole array sorted ascending. Return its length.

**Example**
```
[2,6,4,8,10,9,15] → 5   (sort [6,4,8,10,9])
[1,2,3,4]         → 0
[1]               → 0
```

**Constraints**
* `1 <= nums.length <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-compare-with-a-sorted-copy](v1-compare-with-a-sorted-copy/README.md) | Compare with a sorted copy | `O(n log n)` | `O(n)` | [▶ animation](v1-compare-with-a-sorted-copy/animation/index.html) |
| [v2-two-passes-with-running-max-and-min](v2-two-passes-with-running-max-and-min/README.md) | Two passes with running max and min | `O(n)` | `O(1)` | [▶ animation](v2-two-passes-with-running-max-and-min/animation/index.html) |
