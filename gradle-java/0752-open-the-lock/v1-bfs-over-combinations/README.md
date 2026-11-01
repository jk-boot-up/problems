# 752. Open the Lock — v1: BFS over combinations

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/open-the-lock/)

## Problem

A lock has 4 wheels with digits 0–9; one move turns one wheel one step up or down (wrapping 9 ↔ 0). It starts at `"0000"`. Some
combinations are **deadends** that jam the lock. Return the fewest moves to reach `target`, or `-1`.

**Example**
```
deadends = ["0201","0101","0102","1212","2002"], target = "0202" → 6
deadends = ["8888"], target = "0009" → 1
```

**Constraints**
* `1 <= deadends.length <= 500`; all strings have 4 digits

## Approach: BFS over combinations

> Each of the 10,000 combinations is a node with 8 neighbours; BFS from 0000 avoiding dead ends.

**Shortest path.** BFS from `"0000"` level by level. From each combination generate the 8 one-move neighbours, skipping deadends and
anything already seen (both kept in a `MyHashSet`). The level at which `target` appears is the answer. If `"0000"` itself is a deadend,
nothing is reachable.

* Time: **O(10⁴ · 8 · 4)** — every combination at most once, 8 neighbours of 4 characters.
* Space: **O(10⁴)** — the visited set and queue.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0752/v1/OpenTheLock.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0752/v1/OpenTheLockTest.java` | JUnit 6 tests |
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
