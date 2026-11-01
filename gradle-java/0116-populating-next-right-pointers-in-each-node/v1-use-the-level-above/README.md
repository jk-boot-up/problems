# 116. Populating Next Right Pointers in Each Node — v1: Use the level above

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

## Problem

In a **perfect** binary tree (all leaves on the same level, every parent has two children), set each `next` pointer to the node on its right,
or `null` at the end of a level. Use O(1) extra space.

**Example**
```
[1,2,3,4,5,6,7] → levels linked: 1 → null; 2 → 3 → null; 4 → 5 → 6 → 7 → null
```

**Constraints**
* `0 <= n <= 2^12 - 1`

## Approach: Use the level above

> In a perfect tree, link left → right child, and right child → the next node's left child, level by level.

**Leftmost walk.** For each level starting at `leftmost`, walk it via `next`: set `node.left.next = node.right` and, if `node.next` exists,
`node.right.next = node.next.left`. Move to `leftmost.left`.

* Time: **O(n)** — each node once.
* Space: **O(1)** — pointers only.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0116/v1/PopulatingNextRightPerfect.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0116/v1/PopulatingNextRightPerfectTest.java` | JUnit 6 tests |
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
