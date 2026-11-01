# 1207. Unique Number of Occurrences — v1: Counts + set of counts

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-number-of-occurrences/)

## Problem

Return `true` if the number of occurrences of each value in `arr` is unique.

**Example**
```
[1,2,2,1,1,3] → true (counts 3, 2, 1),   [1,2] → false
```

**Constraints**
* `1 <= arr.length <= 1000`

## Approach: Counts + set of counts

> Count each value, then check that no two values share the same count.

**Two hash structures.** Count with `MyHashMap`; add every count to a `MyHashSet`; a failed add means two values share a count.

* Time: **O(n)** — linear.
* Space: **O(n)** — map and set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1207/v1/UniqueOccurrences.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1207/v1/UniqueOccurrencesTest.java` | JUnit 6 tests |
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
