# 146. LRU Cache — v1: Hash map + doubly linked list

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

## Approach: Hash map + doubly linked list

> A hash map finds nodes in O(1); a doubly linked list keeps them in recency order so the oldest is at the tail.

**`MyHashMap<key, node>` + doubly linked list.** The list runs from most recent (after `head`) to least recent (before `tail`), with two
sentinel nodes so there are no null checks. `get` moves the node to the front. `put` updates or inserts at the front; if the size
exceeds capacity, remove the node before `tail` and delete its key from the map. No `java.util.LinkedHashMap` is used.

* Time: **O(1)** — average per operation: hash lookups plus constant pointer changes.
* Space: **O(capacity)** — one node and one map entry per cached key.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0146/v1/LRUCache.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0146/v1/LRUCacheTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle 9.8.2 project. Only a JDK is needed to start Gradle; JDK 25 is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
