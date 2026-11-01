# 946. Validate Stack Sequences

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/validate-stack-sequences/)

## Problem

Given two arrays `pushed` and `popped` with distinct values, return `true` if they could be the result of a sequence of push and pop
operations on an initially empty stack.

**Example**
```
pushed = [1,2,3,4,5], popped = [4,5,3,2,1] → true
pushed = [1,2,3,4,5], popped = [4,3,5,1,2] → false
```

**Constraints**
* `1 <= n <= 1000`; `popped` is a permutation of `pushed`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-simulate-with-a-stack](v1-simulate-with-a-stack/README.md) | Simulate with a stack | `O(n)` | `O(n)` | [▶ animation](v1-simulate-with-a-stack/animation/index.html) |
