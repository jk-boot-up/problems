# 232. Implement Queue using Stacks — v1: Two stacks, lazy transfer

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/implement-queue-using-stacks/)

## Problem

Implement a FIFO queue (`push`, `pop`, `peek`, `empty`) using only two stacks (push to top, pop/peek from top, size, isEmpty).

**Example**
```
push(1); push(2); peek() → 1; pop() → 1; empty() → false
```

**Constraints**
* At most 100 calls; `pop`/`peek` are only called on a non-empty queue.

**Follow-up:** amortized O(1) per operation.

## Approach: Two stacks, lazy transfer

> Push onto an inbox stack; pop from an outbox stack, refilling it (which reverses the order) only when it is empty.

**Inbox / outbox.** `push` goes onto `in`. `pop`/`peek` read from `out`; if `out` is empty, move everything from `in` to `out`, which reverses
it so the oldest element is on top. Each element moves at most once.

* Time: **O(1)** — amortized per operation.
* Space: **O(n)** — the two stacks.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0232/v1/MyQueue.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0232/v1/MyQueueTest.java` | JUnit 6 tests |
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
