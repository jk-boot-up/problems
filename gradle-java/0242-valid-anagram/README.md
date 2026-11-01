# 242. Valid Anagram

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-anagram/)

## Problem

Return `true` if `t` is an **anagram** of `s`: it uses exactly the same letters, the same number of times, in any order.

**Example 1**
```
Input:  s = "anagram", t = "nagaram"
Output: true
```

**Example 2**
```
Input:  s = "rat", t = "car"
Output: false
```

**Constraints**
* `1 <= s.length, t.length <= 5 * 10^4`; lowercase letters.

**Follow-up:** what if the inputs contain Unicode characters? (Use a hash map instead of a fixed array.)

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-sort-both-strings](v1-sort-both-strings/README.md) | Sort both strings | `O(n log n)` | `O(n)` | [▶ animation](v1-sort-both-strings/animation/index.html) |
| [v2-letter-counts](v2-letter-counts/README.md) | Letter counts | `O(n)` | `O(1)` | [▶ animation](v2-letter-counts/animation/index.html) |
