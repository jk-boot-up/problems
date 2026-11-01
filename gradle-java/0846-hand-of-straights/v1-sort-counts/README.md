# 846. Hand of Straights — v1: Sort + counts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/hand-of-straights/)

## Problem

Can the cards in `hand` be rearranged into groups of `groupSize` **consecutive** values?

**Example**
```
hand = [1,2,3,6,2,3,4,7,8], groupSize = 3 → true ([1,2,3],[2,3,4],[6,7,8])
hand = [1,2,3,4,5], groupSize = 4          → false
```

**Constraints**
* `1 <= hand.length <= 10^4`; `1 <= groupSize <= hand.length`

## Approach: Sort + counts

> The smallest remaining card must start a group, so greedily build groups from the smallest card up.

**Greedy from the smallest.** Count cards in a `MyHashMap` and sort the distinct values. For each value `v` (ascending) with count `c > 0`,
it must start `c` groups: every value `v+1 … v+groupSize-1` needs at least `c` copies, which are then used up.

* Time: **O(n log n)** — sorting dominates.
* Space: **O(n)** — counts and the sorted values.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0846/v1/HandOfStraights.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0846/v1/HandOfStraightsTest.java` | JUnit 6 tests |
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
