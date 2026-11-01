# 1475. Final Prices With a Special Discount in a Shop

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Monotonic Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)

## Problem

Item `i` costs `prices[i]`. Its discount is `prices[j]` for the **first** `j > i` with `prices[j] <= prices[i]` (no discount if none).
Return the final prices.

**Example**
```
[8,4,6,2,3] → [4,2,4,2,3]
[1,2,3,4,5] → [1,2,3,4,5]
[10,1,1,6]  → [9,0,1,6]
```

**Constraints**
* `1 <= prices.length <= 500`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-next-smaller-or-equal-with-a-stack](v1-next-smaller-or-equal-with-a-stack/README.md) | Next smaller-or-equal with a stack | `O(n)` | `O(n)` | [▶ animation](v1-next-smaller-or-equal-with-a-stack/animation/index.html) |
