# 343. Integer Break

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/integer-break/)

## Problem

Break a positive integer `n` into the sum of **at least two** positive integers and maximise their product. Return that product.

**Example**
```
n = 2  → 1   (1 + 1)
n = 10 → 36  (3 + 3 + 4)
```

**Constraints**
* `2 <= n <= 58`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-dynamic-programming](v1-dynamic-programming/README.md) | Dynamic programming | `O(n²)` | `O(n)` | [▶ animation](v1-dynamic-programming/animation/index.html) |
| [v2-greedy-threes](v2-greedy-threes/README.md) | Greedy threes | `O(n)` | `O(1)` | [▶ animation](v2-greedy-threes/animation/index.html) |
