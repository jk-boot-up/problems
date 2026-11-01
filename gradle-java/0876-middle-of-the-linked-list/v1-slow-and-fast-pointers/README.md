# 876. Middle of the Linked List — v1: Slow and fast pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/middle-of-the-linked-list/)

## Problem

Return the middle node of a linked list; with two middle nodes, return the second.

**Example**
```
1→2→3→4→5 → node 3,   1→2→3→4→5→6 → node 4
```

**Constraints**
* `1 <= n <= 100`

## Approach: Slow and fast pointers

> Fast moves two steps for each step of slow; when fast reaches the end, slow is in the middle.

**Tortoise and hare.** Move slow by 1 and fast by 2 while fast and fast.next exist.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0876/v1/MiddleOfLinkedList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0876/v1/MiddleOfLinkedListTest.java` | JUnit 6 tests |
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
