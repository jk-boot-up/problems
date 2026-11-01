# 2462. Total Cost to Hire K Workers — v1: Two heaps from both ends

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/total-cost-to-hire-k-workers/)

## Problem

Hire exactly `k` workers in `k` sessions. In each session, choose the cheapest worker among the first `candidates` and the last `candidates`
remaining workers (ties go to the smaller index). Return the total cost.

**Example**
```
costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4 → 11
costs = [1,2,4,1], k = 3, candidates = 3               → 4
```

**Constraints**
* `1 <= k, candidates <= costs.length <= 10^5`

## Approach: Two heaps from both ends

> Two min-heaps hold the first and last `candidates` workers; each round hire the cheaper top and refill that side.

**Two heaps + two pointers.** Fill `left` with the first `candidates` and `right` with the last (without overlap). Each session, take the
smaller top (left on ties, since it has the smaller index) and refill that heap from its pointer if workers remain between the pointers.

* Time: **O((k + candidates) log candidates)** — heap operations.
* Space: **O(candidates)** — the two heaps.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p2462/v1/TotalCostToHire.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p2462/v1/TotalCostToHireTest.java` | JUnit 6 tests |
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
