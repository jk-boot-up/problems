# 380. Insert Delete GetRandom O(1)

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

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(1)` | `O(n)` | [▶ animation](v1/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
