# 134. Gas Station

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

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Simulate every start | `O(n²)` | `O(1)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Greedy single pass | `O(n)` | `O(1)` | [▶ animation](v2/animation/index.html) |

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
