# 1657. Determine if Two Strings Are Close

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/determine-if-two-strings-are-close/)

## Problem

Two strings are **close** if one can become the other using (1) swaps of any two characters and (2) transforming every occurrence of one
existing letter into another existing letter and vice versa. Return `true` if `word1` and `word2` are close.

**Example**
```
"abc", "bca" → true,   "a", "aa" → false,   "cabbba", "abbccc" → true
```

**Constraints**
* `1 <= length <= 10^5`; lowercase letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-letter-set-sorted-counts](v1-letter-set-sorted-counts/README.md) | Letter set + sorted counts | `O(n)` | `O(1)` | [▶ animation](v1-letter-set-sorted-counts/animation/index.html) |
