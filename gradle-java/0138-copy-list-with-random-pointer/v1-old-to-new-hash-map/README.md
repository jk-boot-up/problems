# 138. Copy List with Random Pointer — v1: Old-to-new hash map

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/)

## Problem

Each node of a linked list has `val`, `next`, and `random`, which points to any node in the list or `null`. Return a **deep copy**:
new nodes with the same values whose `next` and `random` pointers mirror the original structure, never pointing into the original list.

**Example**
```
Input:  [[7,null],[13,0],[11,4],[10,2],[1,0]]   ([val, index of random])
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]   (a separate copy)
```

**Constraints**
* `0 <= n <= 1000`; `-10^4 <= Node.val <= 10^4`

## Approach: Old-to-new hash map

> First create a copy of every node in a map, then wire next and random through the map.

**Hash map from original to copy.** Pass 1 creates every copy and stores `original → copy` in a `MyHashMap`. Pass 2 sets
`copy.next = map.get(original.next)` and `copy.random = map.get(original.random)`.

* Time: **O(n)** — two passes with O(1) average lookups.
* Space: **O(n)** — the map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0138/v1/CopyRandomList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0138/v1/CopyRandomListTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-interleaved-copies](../v2-interleaved-copies/README.md): Interleaved copies (`O(n)` time, `O(1)` space)
