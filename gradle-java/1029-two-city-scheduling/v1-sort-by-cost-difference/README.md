# 1029. Two City Scheduling — v1: Sort by cost difference

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/two-city-scheduling/)

## Problem

`2n` people are interviewing; `costs[i] = [aCost, bCost]` is the cost of flying person `i` to city A or B. Exactly `n` people must go to
each city. Return the minimum total cost.

**Example**
```
[[10,20],[30,200],[400,50],[30,20]] → 110   (A: 10, 30; B: 50, 20)
```

**Constraints**
* `2 <= costs.length <= 100`, even

## Approach: Sort by cost difference

> Sort people by how much cheaper city A is for them; send the first half to A and the rest to B.

**Relative cost.** Imagine everyone flies to B first; sending person `i` to A instead changes the total by `aCost - bCost`. Choose the `n`
people with the smallest (most negative) changes. Sorting by `aCost - bCost` does exactly that.

* Time: **O(n log n)**.
* Space: **O(n)** — the sorted copy.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1029/v1/TwoCityScheduling.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1029/v1/TwoCitySchedulingTest.java` | JUnit 6 tests |
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
