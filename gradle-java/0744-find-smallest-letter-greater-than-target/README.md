# 744. Find Smallest Letter Greater Than Target

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

## Problem

`letters` is sorted (non-decreasing) and contains at least two different letters. Return the smallest letter strictly greater than `target`,
or `letters[0]` if none is.

**Example**
```
letters = [c,f,j], target = a → c;  target = c → f;  letters = [x,x,y,y], target = z → x
```

**Constraints**
* `2 <= letters.length <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-upper-bound-binary-search](v1-upper-bound-binary-search/README.md) | Upper-bound binary search | `O(log n)` | `O(1)` | [▶ animation](v1-upper-bound-binary-search/animation/index.html) |
