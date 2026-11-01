# 125. Valid Palindrome

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-palindrome/)

## Problem

A phrase is a **palindrome** if, after lower-casing it and removing every non-alphanumeric character, it reads the same
forward and backward. Return `true` if `s` is a palindrome.

**Example 1**
```
Input:  s = "A man, a plan, a canal: Panama"
Output: true
```

**Example 2**
```
Input:  s = "race a car"
Output: false
```

**Example 3**
```
Input:  s = " "
Output: true
```

**Constraints**
* `1 <= s.length <= 2 * 10^5`, printable ASCII.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-pointers](v1-two-pointers/README.md) | Two pointers | `O(n)` | `O(1)` | [▶ animation](v1-two-pointers/animation/index.html) |
