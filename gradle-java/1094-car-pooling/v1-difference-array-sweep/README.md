# 1094. Car Pooling — v1: Difference array sweep

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/car-pooling/)

## Problem

A car with `capacity` empty seats drives east only. `trips[i] = [passengers, from, to]` picks up passengers at `from` and drops them at
`to`. Return whether every trip can be served.

**Example**
```
trips = [[2,1,5],[3,3,7]], capacity = 4 → false
trips = [[2,1,5],[3,3,7]], capacity = 5 → true
```

**Constraints**
* `1 <= trips.length <= 1000`, `0 <= from < to <= 1000`

## Approach: Difference array sweep

> Record passenger changes at each pick-up and drop-off point, then sweep the road keeping a running load.

**Difference array.** Add `passengers` at `from` and subtract at `to` (they leave before anyone boards there). Sweep positions `0..1000`
keeping a running sum; if it ever exceeds `capacity`, return `false`.

* Time: **O(n + L)** — `L = 1001` positions.
* Space: **O(L)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1094/v1/CarPooling.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1094/v1/CarPoolingTest.java` | JUnit 6 tests |
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
