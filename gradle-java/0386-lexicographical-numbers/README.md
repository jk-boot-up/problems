# 386. Lexicographical Numbers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Trie &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/lexicographical-numbers/)

## Problem

Return the numbers `1..n` sorted in **lexicographical** (dictionary) order, in O(n) time and O(1) extra space.

**Example**
```
n = 13 → [1,10,11,12,13,2,3,4,5,6,7,8,9]
n = 2  → [1,2]
```

**Constraints**
* `1 <= n <= 5 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-iterative-pre-order-walk](v1-iterative-pre-order-walk/README.md) | Iterative pre-order walk | `O(n)` | `O(1)` | [▶ animation](v1-iterative-pre-order-walk/animation/index.html) |
