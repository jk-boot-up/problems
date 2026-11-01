# 875. Koko Eating Bananas

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/koko-eating-bananas/)

## Problem

Koko eats bananas from `piles` at `k` bananas per hour, finishing one pile before moving on (an hour with fewer than `k` left in a pile is
still a full hour). Return the minimum `k` that lets her finish within `h` hours.

**Example**
```
piles = [3,6,7,11], h = 8 → 4,   piles = [30,11,23,4,20], h = 5 → 30
```

**Constraints**
* `piles.length <= h <= 10^9`; `1 <= piles[i] <= 10^9`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-binary-search-on-the-answer](v1-binary-search-on-the-answer/README.md) | Binary search on the answer | `O(n log M)` | `O(1)` | [▶ animation](v1-binary-search-on-the-answer/animation/index.html) |
