# 997. Find the Town Judge

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-town-judge/)

## Problem

In a town of `n` people, `trust[i] = [a, b]` means `a` trusts `b`. The judge trusts nobody, is trusted by everybody else, and there is
exactly one such person if any. Return the judge's label, or `-1`.

**Example**
```
n = 2, trust = [[1,2]]             → 2
n = 3, trust = [[1,3],[2,3]]       → 3
n = 3, trust = [[1,3],[2,3],[3,1]] → -1
```

**Constraints**
* `1 <= n <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-trust-score](v1-trust-score/README.md) | Trust score | `O(n + t)` | `O(n)` | [▶ animation](v1-trust-score/animation/index.html) |
