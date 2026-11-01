# 705. Design HashSet

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-hashset/)

## Problem

Design a hash set **without** any built-in hash table library: `add(key)`, `contains(key)`, `remove(key)` (removing a missing key does
nothing).

**Example**
```
add(1); add(2); contains(1) → true; contains(3) → false; add(2); contains(2) → true; remove(2); contains(2) → false
```

**Constraints**
* `0 <= key <= 10^6`; at most `10^4` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-separate-chaining-with-resizing](v1-separate-chaining-with-resizing/README.md) | Separate chaining with resizing | `O(1)` | `O(n)` | [▶ animation](v1-separate-chaining-with-resizing/animation/index.html) |
