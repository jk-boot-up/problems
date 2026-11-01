# 779. K-th Symbol in Grammar

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Recursion &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/k-th-symbol-in-grammar/)

## Problem

Row 1 is `0`. Each next row replaces every `0` with `01` and every `1` with `10`. Return the `k`-th (1-indexed) symbol of row `n`.

**Example**
```
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
n = 2, k = 2 → 1;   n = 4, k = 5 → 1
```

**Constraints**
* `1 <= n <= 30`, `1 <= k <= 2^(n-1)`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-recursion-on-the-parent](v1-recursion-on-the-parent/README.md) | Recursion on the parent | `O(n)` | `O(n)` | [▶ animation](v1-recursion-on-the-parent/animation/index.html) |
| [v2-parity-of-the-bits-of-k-1](v2-parity-of-the-bits-of-k-1/README.md) | Parity of the bits of k − 1 | `O(1)` | `O(1)` | [▶ animation](v2-parity-of-the-bits-of-k-1/animation/index.html) |
