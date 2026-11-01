# 225. Implement Stack using Queues — v1: One queue with rotation

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/implement-stack-using-queues/)

## Problem

Implement a LIFO stack (`push`, `pop`, `top`, `empty`) using only queue operations (add to back, remove/peek from front, size, isEmpty).

**Example**
```
push(1); push(2); top() → 2; pop() → 2; empty() → false
```

**Constraints**
* At most 100 calls; `pop`/`top` are only called on a non-empty stack.

## Approach: One queue with rotation

> After adding a new element to the queue, rotate the older ones behind it so the newest is always at the front.

**Rotate on push.** Add `x` at the back, then move the `size - 1` older elements from the front to the back. Now `x` is at the front, so
`pop` and `top` are plain queue operations.

* Time: **O(n)** — per push; pop/top are O(1).
* Space: **O(n)** — the queue.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0225/v1/MyStack.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0225/v1/MyStackTest.java` | JUnit 6 tests |
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
