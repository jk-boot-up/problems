# 706. Design HashMap — v1: Separate chaining with resizing

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

## Approach: Separate chaining with resizing

> An array of buckets indexed by a hash of the key; colliding keys share a bucket's linked list; grow when it gets crowded.

**Buckets + chaining.** Keys are spread with `h ^ (h >>> 16)` and masked to a power-of-two bucket count. Each bucket holds a singly linked
list of `(key, value)` nodes. When the number of entries exceeds 75% of the bucket count, double the array and re-insert every node, which
keeps chains short.

* Time: **O(1)** — average per operation.
* Space: **O(n)** — one node per key plus the bucket array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0706/v1/DesignHashMap.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0706/v1/DesignHashMapTest.java` | JUnit 6 tests |
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
