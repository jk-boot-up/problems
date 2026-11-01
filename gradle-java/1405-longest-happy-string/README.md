# 1405. Longest Happy String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-happy-string/)

## Problem

A string is **happy** if it uses only `'a'`, `'b'`, `'c'`, never contains `"aaa"`, `"bbb"` or `"ccc"`, and uses at most `a`, `b`, `c`
copies of each letter. Return any longest happy string (`""` if none).

**Example**
```
a = 1, b = 1, c = 7 → "ccaccbcc"  (length 8)
a = 7, b = 1, c = 0 → "aabaa"     (length 5)
```

**Constraints**
* `0 <= a, b, c <= 100`, `a + b + c > 0`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-by-remaining-count](v1-greedy-by-remaining-count/README.md) | Greedy by remaining count | `O(a + b + c)` | `O(1)` | [▶ animation](v1-greedy-by-remaining-count/animation/index.html) |
