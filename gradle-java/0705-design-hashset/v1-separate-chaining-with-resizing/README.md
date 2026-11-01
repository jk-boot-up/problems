# 705. Design HashSet — v1: Separate chaining with resizing

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

## Approach: Separate chaining with resizing

> Buckets of chained keys, indexed by a spread hash; double the bucket array when it gets crowded.

**Buckets + chaining.** A power-of-two array of singly linked lists. `index = (h ^ h >>> 16) & (capacity - 1)`. `add` prepends when the key is
absent and doubles the array once the number of keys exceeds 75% of the bucket count.

* Time: **O(1)** — average per operation.
* Space: **O(n)** — one node per key plus the buckets.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0705/v1/DesignHashSet.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0705/v1/DesignHashSetTest.java` | JUnit 6 tests |
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
