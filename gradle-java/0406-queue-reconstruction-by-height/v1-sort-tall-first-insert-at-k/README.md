# 406. Queue Reconstruction by Height — v1: Sort tall-first, insert at k

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/)

## Problem

Each person is `[h, k]`: height `h`, and exactly `k` people **in front** of them have height `>= h`. Reconstruct the queue from a shuffled
list.

**Example**
```
[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] → [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
```

**Constraints**
* `1 <= n <= 2000`; a valid queue always exists

## Approach: Sort tall-first, insert at k

> Place the tallest people first; a shorter person inserted later at index k does not disturb anyone taller.

**Tall first.** Sort by height descending, and by `k` ascending for equal heights. Insert each person at index `k` of the result. Everyone
already placed is at least as tall, so exactly `k` of them end up in front; people inserted later are shorter and invisible to them.

* Time: **O(n²)** — list insertions.
* Space: **O(n)** — the result list.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0406/v1/QueueReconstruction.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0406/v1/QueueReconstructionTest.java` | JUnit 6 tests |
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
