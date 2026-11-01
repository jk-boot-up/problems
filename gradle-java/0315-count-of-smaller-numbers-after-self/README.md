# 315. Count of Smaller Numbers After Self

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Divide and Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

## Problem

For each `nums[i]`, count how many elements to its **right** are strictly smaller. Return the counts.

**Example**
```
[5,2,6,1] → [2,1,1,0]
[-1]      → [0]
[-1,-1]   → [0,0]
```

**Constraints**
* `1 <= nums.length <= 10^5`, `-10^4 <= nums[i] <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-brute-force](v1-brute-force/README.md) | Brute force | `O(n²)` | `O(1)` | [▶ animation](v1-brute-force/animation/index.html) |
| [v2-merge-sort-counting-inversions](v2-merge-sort-counting-inversions/README.md) | Merge sort counting inversions | `O(n log n)` | `O(n)` | [▶ animation](v2-merge-sort-counting-inversions/animation/index.html) |
