# 24. Swap Nodes in Pairs — v1: Iterative re-linking

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/swap-nodes-in-pairs/)

## Problem

Swap every two adjacent nodes of a linked list and return its head. Change the links, not the values.

**Example**
```
1 → 2 → 3 → 4 becomes 2 → 1 → 4 → 3,   1 stays 1,   (empty) stays empty
```

**Constraints**
* `0 <= n <= 100`

## Approach: Iterative re-linking

> With a dummy head, repeatedly re-link the next two nodes in swapped order.

**Dummy + pointer.** `prev` sits before a pair `a → b`. Re-link as `prev → b → a → (rest)` and move `prev` to `a`.

* Time: **O(n)** — each pair once.
* Space: **O(1)** — pointers only.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0024/v1/SwapNodesInPairs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0024/v1/SwapNodesInPairsTest.java` | JUnit 6 tests |
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
