# 767. Reorganize String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reorganize-string/)

## Problem

Rearrange `s` so that no two adjacent characters are equal. Return any valid arrangement, or `""` if none exists.

**Example**
```
"aab"  → "aba"
"aaab" → ""
```

**Constraints**
* `1 <= s.length <= 500`, lower-case letters

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-fill-even-slots-then-odd](v1-fill-even-slots-then-odd/README.md) | Fill even slots, then odd | `O(n)` | `O(n)` | [▶ animation](v1-fill-even-slots-then-odd/animation/index.html) |
