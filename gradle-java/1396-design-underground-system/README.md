# 1396. Design Underground System

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

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-hash-maps](v1-two-hash-maps/README.md) | Two hash maps | `O(L)` | `O(P + S²)` | [▶ animation](v1-two-hash-maps/animation/index.html) |
