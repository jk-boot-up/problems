# 237. Delete Node in a Linked List — v1: Copy the next node

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-node-in-a-linked-list/)

## Problem

You are given only a reference to a node in a singly linked list (not the head). The node is not the tail and all values are unique.
Delete that node's value from the list: afterwards the list should read the same as before, minus that value.

**Example**
```
head = [4,5,1,9], node = 5 → [4,1,9]
head = [4,5,1,9], node = 1 → [4,5,9]
```

**Constraints**
* `2 <= n <= 1000`; the given node is not the last one

## Approach: Copy the next node

> You cannot reach the previous node, so become the next node instead: copy its value and skip it.

**Steal the successor.** Copy `node.next.val` into `node`, then unlink `node.next`. The node that physically disappears is the successor,
but the sequence of values is exactly the list without the deleted value.

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0237/v1/DeleteNode.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0237/v1/DeleteNodeTest.java` | JUnit 6 tests |
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
