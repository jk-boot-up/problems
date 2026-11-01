# 787. Cheapest Flights Within K Stops — v1: Bellman–Ford with k + 1 rounds

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

## Problem

`flights[i] = [from, to, price]`. Return the cheapest price from `src` to `dst` using at most `k` stops (k + 1 flights), or `-1`.

**Example**
```
n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1 → 700
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0 → 500
```

**Constraints**
* `1 <= n <= 100`; `0 <= k < n`

## Approach: Bellman–Ford with k + 1 rounds

> Bellman–Ford limited to k + 1 rounds: round i finds the cheapest prices using at most i flights.

**Bounded relaxation.** Keep `cost[]` (∞ except `src = 0`). Repeat `k + 1` times: copy `cost` to `next`, and for each flight relax
`next[to] = min(next[to], cost[from] + price)`, reading from the **previous** round so each round adds at most one flight.

* Time: **O(k · E)** — k + 1 rounds over all flights.
* Space: **O(n)** — two price arrays.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0787/v1/CheapestFlights.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0787/v1/CheapestFlightsTest.java` | JUnit 6 tests |
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
