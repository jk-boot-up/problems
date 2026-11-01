# 981. Time Based Key-Value Store

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/time-based-key-value-store/)

## Problem

Implement `TimeMap`:
* `set(key, value, timestamp)` stores a value; timestamps for set calls are strictly increasing;
* `get(key, timestamp)` returns the value set for `key` at the largest `timestamp_prev <= timestamp`, or `""` if none.

**Example**
```
set("foo","bar",1); get("foo",1) → "bar"; get("foo",3) → "bar";
set("foo","bar2",4); get("foo",4) → "bar2"; get("foo",5) → "bar2"
```

**Constraints**
* `1 <= timestamp <= 10^7`; at most `2 * 10^5` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-map-of-sorted-lists](v1-hash-map-of-sorted-lists/README.md) | Hash map of sorted lists | `O(log n)` | `O(n)` | [▶ animation](v1-hash-map-of-sorted-lists/animation/index.html) |
