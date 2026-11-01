# 205. Isomorphic Strings

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/isomorphic-strings/)

## Problem

Two strings `s` and `t` are **isomorphic** if the characters of `s` can be replaced to get `t`: every occurrence of a character
is replaced by the same character, and no two different characters map to the same character (a character may map to itself).

**Example 1**
```
Input:  s = "egg", t = "add"
Output: true
```

**Example 2**
```
Input:  s = "foo", t = "bar"
Output: false
```

**Example 3**
```
Input:  s = "paper", t = "title"
Output: true
```

**Constraints**
* `1 <= s.length <= 5 * 10^4`, `t.length == s.length`; any ASCII characters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-way-mapping](v1-two-way-mapping/README.md) | Two-way mapping | `O(n)` | `O(1)` | [▶ animation](v1-two-way-mapping/animation/index.html) |
