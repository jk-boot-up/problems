# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Problem

`numbers` is sorted in non-decreasing order (1-indexed). Find two different positions `index1 < index2` whose values add up to
`target`, and return `[index1, index2]` (1-based). Exactly one solution exists. Use only constant extra space.

**Example 1**
```
Input:  numbers = [2,7,11,15], target = 9
Output: [1,2]
```

**Example 2**
```
Input:  numbers = [-1,0], target = -1
Output: [1,2]
```

**Constraints**
* `2 <= numbers.length <= 3 * 10^4`
* `-1000 <= numbers[i], target <= 1000`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-for-the-partner](v1-binary-search-for-the-partner/README.md) | Binary search for the partner | `O(n log n)` | `O(1)` | [▶ animation](v1-binary-search-for-the-partner/animation/index.html) |
| [v2-two-pointers](v2-two-pointers/README.md) | Two pointers | `O(n)` | `O(1)` | [▶ animation](v2-two-pointers/animation/index.html) |
