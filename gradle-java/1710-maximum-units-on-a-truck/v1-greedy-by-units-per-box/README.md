# 1710. Maximum Units on a Truck — v1: Greedy by units per box

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-units-on-a-truck/)

## Problem

`boxTypes[i] = [count, unitsPerBox]`. A truck holds at most `truckSize` boxes. Return the maximum total units it can carry.

**Example**
```
boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4 → 8
boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10 → 91
```

**Constraints**
* `1 <= boxTypes.length <= 1000`, `1 <= count, unitsPerBox <= 1000`, `1 <= truckSize <= 10^6`

## Approach: Greedy by units per box

> Load the boxes with the most units per box first.

**Best boxes first.** Every box takes one slot, so a box with more units is always at least as good. Unit counts are at most 1000, so
bucket the box counts by units (no comparison sort needed) and load from 1000 down until the truck is full.

* Time: **O(n + U)** — `U = 1000`.
* Space: **O(U)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1710/v1/MaximumUnitsOnTruck.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1710/v1/MaximumUnitsOnTruckTest.java` | JUnit 6 tests |
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
