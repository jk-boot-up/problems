# 950. Reveal Cards In Increasing Order — v1: Simulate on indices

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Queue &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reveal-cards-in-increasing-order/)

## Problem

A deck is revealed like this: reveal the top card and remove it, then move the next top card to the bottom; repeat until empty. Order the
deck so the cards are revealed in **increasing** order.

**Example**
```
[17,13,11,2,3,5,7] → [2,13,3,11,5,17,7]
```

**Constraints**
* `1 <= deck.length <= 1000`, distinct values

## Approach: Simulate on indices

> Simulate the reveal process on positions instead of cards, then drop the sorted cards into the positions in reveal order.

**Positions.** Put positions `0..n-1` in a queue. Run the process on the queue: the position at the front is revealed next (give it the
next smallest card), then the following position moves to the back.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the queue.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0950/v1/RevealCardsIncreasing.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0950/v1/RevealCardsIncreasingTest.java` | JUnit 6 tests |
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
