# 22. Generate Parentheses

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/generate-parentheses/)

## Problem

Given `n` pairs of parentheses, generate all combinations of **well-formed** parentheses.

**Example**
```
Input:  n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Constraints**
* `1 <= n <= 8`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-backtracking-with-open-close-counts](v1-backtracking-with-open-close-counts/README.md) | Backtracking with open/close counts | `O(4ⁿ / √n)` | `O(n)` | [▶ animation](v1-backtracking-with-open-close-counts/animation/index.html) |
