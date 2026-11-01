# 2108. Find First Palindromic String in the Array

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)

## Problem

Return the first string in `words` that is a palindrome, or `""` if there is none.

**Example**
```
["abc","car","ada","racecar","cool"] → "ada"
["notapalindrome","racecar"]         → "racecar"
["def","ghi"]                        → ""
```

**Constraints**
* `1 <= words.length <= 100`, `1 <= words[i].length <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-pointer-check-per-word](v1-two-pointer-check-per-word/README.md) | Two-pointer check per word | `O(total length)` | `O(1)` | [▶ animation](v1-two-pointer-check-per-word/animation/index.html) |
