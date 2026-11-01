# 117. Populating Next Right Pointers in Each Node II — v1: BFS with a queue

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

## Problem

Each node of a binary tree has an extra pointer `next`. Set every `next` to the node immediately to its right on the same level, or
to `null` if there is none. The tree is not necessarily perfect.

**Example**
```
Input:  [1,2,3,4,5,null,7]
Output: levels linked as  1 → null,  2 → 3 → null,  4 → 5 → 7 → null
```

**Constraints**
* `0 <= n <= 6000`; `-100 <= Node.val <= 100`

**Follow-up:** constant extra space (the recursion stack does not count).

## Approach: BFS with a queue

> Process the tree level by level; link each node to the next one in its level.

**Level-order queue.** For each level, pop its nodes in order and set `prev.next = node`.

* Time: **O(n)** — each node is enqueued once.
* Space: **O(w)** — the queue holds a whole level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0117/v1/PopulatingNextRight.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0117/v1/PopulatingNextRightTest.java` | JUnit 6 tests |
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

* [v2-level-walk-with-o-1-space](../v2-level-walk-with-o-1-space/README.md): Level walk with O(1) space (`O(n)` time, `O(1)` space)
