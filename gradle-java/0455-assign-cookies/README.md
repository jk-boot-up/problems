# 455. Assign Cookies

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/assign-cookies/)

## Problem

Child `i` is content with a cookie of size at least `g[i]`. Cookie `j` has size `s[j]`. Each child gets at most one cookie. Return the
maximum number of content children.

**Example**
```
g = [1,2,3], s = [1,1]   → 1
g = [1,2],   s = [1,2,3] → 2
```

**Constraints**
* `1 <= g.length <= 3 * 10^4`, `0 <= s.length <= 3 * 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-and-two-pointers](v1-sort-and-two-pointers/README.md) | Sort and two pointers | `O(n log n + m log m)` | `O(1)` | [▶ animation](v1-sort-and-two-pointers/animation/index.html) |
