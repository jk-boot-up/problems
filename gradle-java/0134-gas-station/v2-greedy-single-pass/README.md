# 134. Gas Station — v2: Greedy single pass

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

## Approach: Greedy single pass

> If total gas ≥ total cost a solution exists; whenever the tank goes negative, the start must be after this station.

**Greedy single pass.** Track `total = Σ(gas - cost)`; if it is negative, no start works. Also track the current `tank`
from a candidate `start`. If `tank` drops below 0 at station `i`, no station between `start` and `i` can be the start
(each would arrive at `i` with even less fuel), so set `start = i + 1` and reset the tank.

* Time: **O(n)** — one pass around the stations.
* Space: **O(1)** — three running numbers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0134/v2/GasStation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0134/v2/GasStationTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-simulate-every-start](../v1-simulate-every-start/README.md): Simulate every start (`O(n²)` time, `O(1)` space)
