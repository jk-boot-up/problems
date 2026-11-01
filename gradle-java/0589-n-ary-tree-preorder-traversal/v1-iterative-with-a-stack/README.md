# 589. N-ary Tree Preorder Traversal — v1: Iterative with a stack

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

## Problem

Return the preorder traversal (node, then its children left to right) of an n-ary tree.

The tree uses `NaryPreorder.Node`, which has `val` and `children`.

**Example**
```
1
├─ 3
│  ├─ 5
│  └─ 6
├─ 2
└─ 4                → [1,3,5,6,2,4]
```

**Constraints**
* `0 <= n <= 10^4`, height at most 1000

## Approach: Iterative with a stack

> Use a stack; push children in reverse so the leftmost child is processed first.

**Explicit stack.** Pop a node, record it, then push its children from right to left so the leftmost child is on top. This avoids deep
recursion.

* Time: **O(n)**.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0589/v1/NaryPreorder.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0589/v1/NaryPreorderTest.java` | JUnit 6 tests |
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
