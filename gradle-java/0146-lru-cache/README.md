# 146. LRU Cache

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/lru-cache/)

## Problem

Design a **Least Recently Used** cache with a fixed `capacity`:
* `int get(int key)`: return the value if the key exists, otherwise `-1`. A successful get marks the key as most recently used.
* `void put(int key, int value)`: insert or update the key. If this exceeds the capacity, evict the **least recently used** key.

Both operations must run in **O(1)** average time.

**Example**
```
LRUCache(2); put(1,1); put(2,2); get(1) → 1; put(3,3) evicts 2; get(2) → -1;
put(4,4) evicts 1; get(1) → -1; get(3) → 3; get(4) → 4
```

**Constraints**
* `1 <= capacity <= 3000`; at most `2 * 10^5` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-hash-map-doubly-linked-list](v1-hash-map-doubly-linked-list/README.md) | Hash map + doubly linked list | `O(1)` | `O(capacity)` | [▶ animation](v1-hash-map-doubly-linked-list/animation/index.html) |
