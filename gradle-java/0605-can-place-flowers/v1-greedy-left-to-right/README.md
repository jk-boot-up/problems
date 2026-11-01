# 605. Can Place Flowers — v1: Greedy left to right

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/can-place-flowers/)

## Problem

A flowerbed is an array of `0` (empty) and `1` (planted); flowers may not be adjacent. Return `true` if `n` new flowers can be planted.

**Example**
```
flowerbed = [1,0,0,0,1], n = 1 → true
flowerbed = [1,0,0,0,1], n = 2 → false
```

**Constraints**
* `1 <= flowerbed.length <= 2 * 10^4`

## Approach: Greedy left to right

> Plant greedily in every empty plot whose neighbours are empty too.

**Greedy.** Scan left to right; plant in plot `i` when it and both neighbours (treating the ends as empty) are `0`. Planting as early as
possible never blocks a better arrangement.

* Time: **O(n)** — one pass.
* Space: **O(1)** — works on a copy only to avoid changing the input.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0605/v1/CanPlaceFlowers.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0605/v1/CanPlaceFlowersTest.java` | JUnit 6 tests |
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
