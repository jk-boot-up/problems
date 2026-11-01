# 981. Time Based Key-Value Store — v1: Hash map of sorted lists

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

## Approach: Hash map of sorted lists

> Keep each key's (timestamp, value) list in increasing time order; get binary-searches the latest timestamp ≤ t.

**`MyHashMap<key, list>`.** Because timestamps only increase, appending keeps each list sorted. `get` binary-searches the last entry with
`time <= timestamp`.

* Time: **O(log n)** — per get (set is O(1) amortized).
* Space: **O(n)** — every stored value.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0981/v1/TimeMap.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0981/v1/TimeMapTest.java` | JUnit 6 tests |
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
