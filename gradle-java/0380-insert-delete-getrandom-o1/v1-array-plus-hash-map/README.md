# 380. Insert Delete GetRandom O(1) — v1: Array plus hash map

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## Problem

Implement `RandomizedSet`:
* `boolean insert(int val)`: inserts `val` if absent. Returns `true` if it was inserted.
* `boolean remove(int val)`: removes `val` if present. Returns `true` if it was removed.
* `int getRandom()`: returns a random element (the set is non-empty when called); each element must be equally likely.

Every operation must run in **average O(1)** time.

**Example**
```
insert(1) → true, remove(2) → false, insert(2) → true, getRandom() → 1 or 2,
remove(1) → true, insert(2) → false, getRandom() → 2
```

**Constraints**
* `-2^31 <= val <= 2^31 - 1`
* At most `2 * 10^5` calls in total.

## Approach: Array plus hash map

> An array gives O(1) random picks; a value→index map gives O(1) lookups; delete by swapping with the last element.

**ArrayList + hash map.** We use our own `MyHashMap` (bucket array + chaining). The list stores values so `getRandom` picks a random index. The map stores each value's index.
To remove `val`, move the **last** value into `val`'s slot, update that value's index, and drop the last slot. Nothing shifts.

* Time: **O(1)** — average per operation (hash map + array end operations).
* Space: **O(n)** — the list and the map each hold every stored value.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0380/v1/RandomizedSet.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0380/v1/RandomizedSetTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
