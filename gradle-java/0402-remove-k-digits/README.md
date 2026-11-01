# 402. Remove K Digits

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Monotonic Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-k-digits/)

## Problem

Given a non-negative integer as a string `num` and an integer `k`, remove `k` digits so the remaining number is as small as possible.
Return it without leading zeros (`"0"` if nothing is left).

**Example**
```
num = "1432219", k = 3 → "1219"
num = "10200",   k = 1 → "200"
num = "10",      k = 2 → "0"
```

**Constraints**
* `1 <= k <= num.length <= 10^5`; `num` has no leading zeros except `"0"` itself

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-monotonic-increasing-stack](v1-monotonic-increasing-stack/README.md) | Monotonic increasing stack | `O(n)` | `O(n)` | [▶ animation](v1-monotonic-increasing-stack/animation/index.html) |
