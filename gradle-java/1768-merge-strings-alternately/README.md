# 1768. Merge Strings Alternately

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-strings-alternately/)

## Problem

Merge `word1` and `word2` by alternating their letters, starting with `word1`. If one is longer, append its remaining letters.

**Example**
```
"abc", "pqr"  → "apbqcr"
"ab", "pqrs"  → "apbqrs"
```

**Constraints**
* `1 <= word1.length, word2.length <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-alternating-pointers](v1-alternating-pointers/README.md) | Alternating pointers | `O(m + n)` | `O(m + n)` | [▶ animation](v1-alternating-pointers/animation/index.html) |
