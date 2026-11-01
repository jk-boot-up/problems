# 443. String Compression

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/string-compression/)

## Problem

Compress `chars` in place: each run of a repeated character becomes the character followed by the run length (if the length is more than
1, written digit by digit). Return the new length.

**Example**
```
["a","a","b","b","c","c","c"] → 6, chars = ["a","2","b","2","c","3"]
["a"]                          → 1
["a","b","b","b","b","b","b","b","b","b","b","b","b"] → 4 ("a","b","1","2")
```

**Constraints**
* `1 <= chars.length <= 2000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-read-write-pointers](v1-read-write-pointers/README.md) | Read/write pointers | `O(n)` | `O(1)` | [▶ animation](v1-read-write-pointers/animation/index.html) |
