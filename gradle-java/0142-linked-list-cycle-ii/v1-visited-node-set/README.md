# 142. Linked List Cycle II — v1: Visited-node set

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/)

## Problem

Return the node where the cycle in a linked list begins, or `null` if there is no cycle. Do not modify the list.

**Example**
```
3 → 2 → 0 → -4 → (back to 2)   → the node with value 2
1 → 2 → (back to 1)            → the node with value 1
```

**Constraints**
* `0 <= n <= 10^4`

**Follow-up:** O(1) memory.

## Approach: Visited-node set

> The first node visited twice is the start of the cycle.

**`MyHashSet` of nodes.** Walk the list; the first node already in the set is where the cycle begins.

* Time: **O(n)** — each node once.
* Space: **O(n)** — the set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0142/v1/LinkedListCycleII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0142/v1/LinkedListCycleIITest.java` | JUnit 6 tests |
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

* [v2-floyd-meet-then-find-the-entrance](../v2-floyd-meet-then-find-the-entrance/README.md): Floyd: meet, then find the entrance (`O(n)` time, `O(1)` space)
