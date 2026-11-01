# 71. Simplify Path

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/simplify-path/)

## Problem

Convert an absolute Unix-style `path` to its **canonical** form:
* `.` means the current directory and `..` the parent directory (staying at `/` if already there);
* multiple slashes count as one; other names, including `...`, are directory names;
* the result starts with one `/`, separates directories with single slashes and has no trailing slash.

**Example 1**
```
Input:  path = "/home//foo/"
Output: "/home/foo"
```

**Example 2**
```
Input:  path = "/a/./b/../../c/"
Output: "/c"
```

**Example 3**
```
Input:  path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
```

**Constraints**
* `1 <= path.length <= 3000`; letters, digits, `.`, `/`, `_`; starts with `/`.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-stack-of-directories](v1-stack-of-directories/README.md) | Stack of directories | `O(n)` | `O(n)` | [▶ animation](v1-stack-of-directories/animation/index.html) |
