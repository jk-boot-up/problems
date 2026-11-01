# 134. Gas Station — v1: Simulate every start

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/gas-station/)

## Problem

There are `n` gas stations on a circular route. Station `i` gives `gas[i]` fuel, and driving from station `i` to `i + 1`
costs `cost[i]`. Starting with an empty tank, return the index of the station from which you can drive all the way around
once, or `-1` if impossible. If a solution exists it is unique.

**Example 1**
```
Input:  gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
```

**Example 2**
```
Input:  gas = [2,3,4], cost = [3,4,3]
Output: -1
```

**Constraints**
* `1 <= n <= 10^5`
* `0 <= gas[i], cost[i] <= 10^4`

## Approach: Simulate every start

> Try each station as the start and drive around until the tank runs dry.

**Brute force.** For every start `s`, drive `n` legs, adding `gas` and subtracting `cost`. If the tank never drops below zero,
`s` works.

* Time: **O(n²)** — n starts × up to n legs.
* Space: **O(1)** — a tank counter.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0134/v1/GasStation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0134/v1/GasStationTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-greedy-single-pass](../v2-greedy-single-pass/README.md): Greedy single pass (`O(n)` time, `O(1)` space)
