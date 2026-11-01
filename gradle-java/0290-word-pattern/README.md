# 290. Word Pattern

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-pattern/)

## Problem

Given a `pattern` of letters and a string `s` of space-separated words, return `true` if `s` **follows** the pattern: there is a
one-to-one correspondence between pattern letters and words.

**Example 1**
```
Input:  pattern = "abba", s = "dog cat cat dog"
Output: true
```

**Example 2**
```
Input:  pattern = "abba", s = "dog cat cat fish"
Output: false
```

**Example 3**
```
Input:  pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

**Constraints**
* `1 <= pattern.length <= 300`; `1 <= s.length <= 3000`; words are lowercase and separated by single spaces.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-way-mapping](v1-two-way-mapping/README.md) | Two-way mapping | `O(n)` | `O(n)` | [▶ animation](v1-two-way-mapping/animation/index.html) |
