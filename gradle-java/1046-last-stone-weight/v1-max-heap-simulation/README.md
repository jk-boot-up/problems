# 1046. Last Stone Weight — v1: Max-heap simulation

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/last-stone-weight/)

## Problem

Repeatedly smash the two heaviest stones `x <= y`: if equal, both vanish; otherwise a stone of weight `y - x` remains. Return the weight of
the last stone, or 0 if none remain.

**Example**
```
[2,7,4,1,8,1] → 1
```

**Constraints**
* `1 <= stones.length <= 30`

## Approach: Max-heap simulation

> A max-heap always hands you the two heaviest stones to smash.

**Max-heap.** Pop the two largest; push their difference if non-zero. Stop when at most one stone is left.

* Time: **O(n log n)** — about n rounds of heap operations.
* Space: **O(n)** — the heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1046/v1/LastStoneWeight.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1046/v1/LastStoneWeightTest.java` | JUnit 6 tests |
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
