# 25. Reverse Nodes in k-Group — v1: Iterative group reversal

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Problem

Reverse the nodes of a linked list `k` at a time and return the new head. If the number of remaining nodes is less than `k`,
leave them as they are. Only change the links, not the values.

**Example 1**
```
Input:  head = 1 → 2 → 3 → 4 → 5, k = 2
Output: 2 → 1 → 4 → 3 → 5
```

**Example 2**
```
Input:  head = 1 → 2 → 3 → 4 → 5, k = 3
Output: 3 → 2 → 1 → 4 → 5
```

**Constraints**
* `1 <= k <= n <= 5000`

**Follow-up:** O(1) extra memory.

## Approach: Iterative group reversal

> For each full group of k nodes, reverse it in place and stitch it between the previous group and the rest.

**Group by group.** `groupPrev` is the node before the current group. Check that `k` nodes follow; if not, stop. Reverse those `k`
nodes with the usual three-pointer loop, then connect `groupPrev` to the new group head and the old group head (now the tail) to
the next group. Move `groupPrev` to that tail.

* Time: **O(n)** — each node is checked once and reversed once.
* Space: **O(1)** — a fixed number of pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0025/v1/ReverseKGroup.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0025/v1/ReverseKGroupTest.java` | JUnit 6 tests |
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
