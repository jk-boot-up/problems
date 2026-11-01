# 2300. Successful Pairs of Spells and Potions

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

## Problem

A spell and potion pair succeeds if `spell × potion >= success`. For each spell, return how many potions form a successful pair with it.

**Example**
```
spells = [5,1,3], potions = [1,2,3,4,5], success = 7 → [4,0,3]
```

**Constraints**
* `1 <= n, m <= 10^5`; `1 <= success <= 10^10`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-binary-search](v1-sort-binary-search/README.md) | Sort + binary search | `O((n + m) log m)` | `O(m)` | [▶ animation](v1-sort-binary-search/animation/index.html) |
