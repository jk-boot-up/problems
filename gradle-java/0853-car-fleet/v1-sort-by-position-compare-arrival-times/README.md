# 853. Car Fleet — v1: Sort by position, compare arrival times

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/car-fleet/)

## Problem

Cars on a one-lane road drive toward `target`. Car `i` starts at `position[i]` with speed `speed[i]`. A faster car that catches a slower
one slows down and they move together as a **fleet**. Return the number of fleets that reach the target.

**Example**
```
target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3] → 3
```

**Constraints**
* `1 <= n <= 10^5`; positions are distinct and `< target`.

## Approach: Sort by position, compare arrival times

> Sort cars from closest to the target; a car that would arrive no later than the fleet ahead joins it.

**Arrival times.** Sort cars by position, closest to the target first. Each car's solo arrival time is `(target - position) / speed`. Walk
from the front: if a car's time is greater than the current fleet's time, it can never catch up and starts a new fleet; otherwise it joins.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the sorted order.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0853/v1/CarFleet.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0853/v1/CarFleetTest.java` | JUnit 6 tests |
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
