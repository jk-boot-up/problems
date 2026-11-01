# 706. Design HashMap

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-hashmap/)

## Problem

Design a hash map **without** any built-in hash table library:
* `put(key, value)`: insert or update;
* `get(key)`: the value, or `-1` if the key is absent;
* `remove(key)`.

**Example**
```
put(1,1); put(2,2); get(1) → 1; get(3) → -1; put(2,1); get(2) → 1; remove(2); get(2) → -1
```

**Constraints**
* `0 <= key, value <= 10^6`; at most `10^4` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-separate-chaining-with-resizing](v1-separate-chaining-with-resizing/README.md) | Separate chaining with resizing | `O(1)` | `O(n)` | [▶ animation](v1-separate-chaining-with-resizing/animation/index.html) |
