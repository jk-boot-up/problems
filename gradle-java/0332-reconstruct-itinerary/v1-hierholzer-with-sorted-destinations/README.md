# 332. Reconstruct Itinerary — v1: Hierholzer with sorted destinations

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reconstruct-itinerary/)

## Problem

Given airline `tickets[i] = [from, to]`, use **all** tickets exactly once to build an itinerary starting at `"JFK"`. If several are valid,
return the lexicographically smallest. At least one valid itinerary exists.

**Example**
```
[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] → ["JFK","MUC","LHR","SFO","SJC"]
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] → ["JFK","ATL","JFK","SFO","ATL","SFO"]
```

**Constraints**
* `1 <= tickets.length <= 300`

## Approach: Hierholzer with sorted destinations

> Hierholzer's algorithm: take the smallest unused ticket each time; airports are added when they run out of tickets, giving the route in reverse.

**Eulerian path.** Map each airport to a min-heap of destinations (`MyHashMap<String, PriorityQueue<String>>`). With an explicit stack,
keep flying the smallest unused ticket from the top airport; when an airport has no tickets left, pop it onto the front of the answer.
Dead ends are therefore placed last, which is why the greedy choice still uses every ticket.

* Time: **O(E log E)** — each ticket is pushed and popped from a heap once.
* Space: **O(E)** — the graph and the stack.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0332/v1/ReconstructItinerary.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0332/v1/ReconstructItineraryTest.java` | JUnit 6 tests |
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
