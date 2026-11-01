# 1396. Design Underground System — v1: Two hash maps

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-underground-system/)

## Problem

Implement `UndergroundSystem`:

* `checkIn(int id, String station, int t)` and `checkOut(int id, String station, int t)` — a customer can be checked in to one place at a
  time.
* `double getAverageTime(String start, String end)` — the average time of all completed trips from `start` to `end` (at least one exists).

**Example**
```
checkIn(45,"Leyton",3); checkIn(32,"Paradise",8); checkIn(27,"Leyton",10);
checkOut(45,"Waterloo",15); checkOut(27,"Waterloo",20); checkOut(32,"Cambridge",22);
getAverageTime("Paradise","Cambridge") → 14.0
getAverageTime("Leyton","Waterloo") → 11.0
```

**Constraints**
* Up to `2 * 10^4` calls; station names are 1–10 letters

## Approach: Two hash maps

> Remember each open trip by card id; on check-out, add the trip time to a running total for the station pair.

**Two maps.** `open` maps a card id to its check-in station and time. On check-out, remove it and add the duration to `stats` for the key
`start + "," + end`, which holds a total and a count. The average is `total / count`. Both maps are `MyHashMap`.

* Time: **O(L)** — per call, for building and hashing the station key.
* Space: **O(P + S²)** — open trips and station pairs.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1396/v1/UndergroundSystem.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1396/v1/UndergroundSystemTest.java` | JUnit 6 tests |
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
