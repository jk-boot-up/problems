# 202. Happy Number

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/happy-number/)

## Problem

A number is **happy** if repeatedly replacing it with the sum of the squares of its digits eventually reaches `1`. Numbers that
never reach 1 loop forever in a cycle. Return `true` if `n` is happy.

**Example 1**
```
Input:  n = 19
Output: true   (1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1)
```

**Example 2**
```
Input:  n = 2
Output: false
```

**Constraints**
* `1 <= n <= 2^31 - 1`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-seen-set](v1-seen-set/README.md) | Seen set | `O(log n)` | `O(log n)` | [▶ animation](v1-seen-set/animation/index.html) |
| [v2-floyd-cycle-detection](v2-floyd-cycle-detection/README.md) | Floyd cycle detection | `O(log n)` | `O(1)` | [▶ animation](v2-floyd-cycle-detection/animation/index.html) |
