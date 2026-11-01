# 384. Shuffle an Array

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Randomized &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/shuffle-an-array/)

## Problem

Implement `ShuffleArray`:

* `ShuffleArray(int[] nums)`
* `int[] reset()` — the original array.
* `int[] shuffle()` — a random permutation; all `n!` permutations equally likely.

**Example**
```
nums = [1,2,3]
shuffle() → e.g. [3,1,2], reset() → [1,2,3], shuffle() → e.g. [1,3,2]
```

**Constraints**
* `1 <= nums.length <= 50`, values unique

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-fisher-yates-shuffle](v1-fisher-yates-shuffle/README.md) | Fisher–Yates shuffle | `O(n)` | `O(n)` | [▶ animation](v1-fisher-yates-shuffle/animation/index.html) |
