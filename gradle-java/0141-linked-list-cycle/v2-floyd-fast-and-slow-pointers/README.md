# 141. Linked List Cycle — v2: Floyd fast and slow pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/linked-list-cycle/)

## Problem

Given the `head` of a linked list, return `true` if the list has a **cycle**: some node can be reached again by following `next`.

**Example 1**
```
Input:  3 → 2 → 0 → -4 → (back to 2)
Output: true
```

**Example 2**
```
Input:  1 → 2 → null
Output: false
```

**Constraints**
* `0 <= number of nodes <= 10^4`

**Follow-up:** O(1) memory.

## Approach: Floyd fast and slow pointers

> A fast pointer (two steps) laps a slow pointer (one step) only if the list loops.

**Floyd's tortoise and hare.** Move `slow` one step and `fast` two steps. If `fast` reaches `null` there is no cycle. Inside a cycle,
the gap between them shrinks by one each step, so they must meet.

* Time: **O(n)** — fast enters the cycle within n steps and catches slow within one lap.
* Space: **O(1)** — two pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0141/v2/LinkedListCycle.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0141/v2/LinkedListCycleTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-visited-node-set](../v1-visited-node-set/README.md): Visited-node set (`O(n)` time, `O(n)` space)
