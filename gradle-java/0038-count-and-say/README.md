# 38. Count and Say

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Strings &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-and-say/)

## Problem

`countAndSay(1) = "1"`; `countAndSay(n)` describes `countAndSay(n-1)` by saying, for each run of equal digits, the run length followed by the
digit. Return the `n`-th term.

**Example**
```
1 → "1",   2 → "11",   3 → "21",   4 → "1211",   5 → "111221"
```

**Constraints**
* `1 <= n <= 30`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-run-length-encoding](v1-run-length-encoding/README.md) | Run-length encoding | `O(L)` | `O(L)` | [▶ animation](v1-run-length-encoding/animation/index.html) |
