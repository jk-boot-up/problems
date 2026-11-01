# 2095. Delete the Middle Node of a Linked List — v1: Slow and fast pointers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

## Problem

Delete the middle node (index `⌊n/2⌋`, 0-based) of a linked list and return the head.

**Example**
```
1→3→4→7→1→2→6 becomes 1→3→4→1→2→6,   1→2→3→4 becomes 1→2→4,   2→1 becomes 2
```

**Constraints**
* `1 <= n <= 10^5`

## Approach: Slow and fast pointers

> Start fast one step ahead so slow stops just before the middle, then unlink it.

**Offset pointers.** With one node, return null. Otherwise start `slow = head`, `fast = head.next.next`; advance slow by 1 and fast by 2.
When fast runs out, `slow.next` is the middle: skip it.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p2095/v1/DeleteMiddleNode.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p2095/v1/DeleteMiddleNodeTest.java` | JUnit 6 tests |
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
