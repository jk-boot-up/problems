# 763. Partition Labels

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/partition-labels/)

## Problem

Split `s` into as many parts as possible so that each letter appears in at most one part. Return the part sizes in order.

**Example**
```
"ababcbacadefegdehijhklij" → [9,7,8]
"eccbbbbdec"               → [10]
```

**Constraints**
* `1 <= s.length <= 500`; lowercase letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-last-occurrence-greedy](v1-last-occurrence-greedy/README.md) | Last-occurrence greedy | `O(n)` | `O(1)` | [▶ animation](v1-last-occurrence-greedy/animation/index.html) |
