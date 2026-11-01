# 380. Insert Delete GetRandom O(1)

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## Problem

Implement `RandomizedSet`:
* `boolean insert(int val)`: inserts `val` if absent. Returns `true` if it was inserted.
* `boolean remove(int val)`: removes `val` if present. Returns `true` if it was removed.
* `int getRandom()`: returns a random element (the set is non-empty when called); each element must be equally likely.

Every operation must run in **average O(1)** time.

**Example**
```
insert(1) → true, remove(2) → false, insert(2) → true, getRandom() → 1 or 2,
remove(1) → true, insert(2) → false, getRandom() → 2
```

**Constraints**
* `-2^31 <= val <= 2^31 - 1`
* At most `2 * 10^5` calls in total.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-array-plus-hash-map](v1-array-plus-hash-map/README.md) | Array plus hash map | `O(1)` | `O(n)` | [▶ animation](v1-array-plus-hash-map/animation/index.html) |
