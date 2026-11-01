# 383. Ransom Note

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ransom-note/)

## Problem

Return `true` if `ransomNote` can be built from the letters of `magazine`, using each magazine letter at most once.

**Example 1**
```
Input:  ransomNote = "a", magazine = "b"
Output: false
```

**Example 2**
```
Input:  ransomNote = "aa", magazine = "aab"
Output: true
```

**Constraints**
* `1 <= ransomNote.length, magazine.length <= 10^5`; lowercase letters.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-letter-counts](v1-letter-counts/README.md) | Letter counts | `O(m + n)` | `O(1)` | [▶ animation](v1-letter-counts/animation/index.html) |
