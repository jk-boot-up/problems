# 1325. Delete Leaves With a Given Value — v1: Post-order pruning

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/delete-leaves-with-a-given-value/)

## Problem

Delete every leaf whose value is `target`. If deleting leaves turns a parent into a target-valued leaf, delete it too, and so on.

**Example**
```
[1,2,3,2,null,2,4], target = 2 → [1,null,3,null,4]
[1,3,3,3,2],        target = 3 → [1,3,null,null,2]
[1,2,null,2,null,2], target = 2 → [1]
```

**Constraints**
* `1 <= n <= 3000`

## Approach: Post-order pruning

> Clean the children first; a node that becomes a leaf with the target value is then removed too.

**Bottom-up.** Recurse into both children first and replace them with the pruned results. Only then check the node itself: if it has no
children left and its value is `target`, return `null`.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1325/v1/DeleteLeavesWithValue.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1325/v1/DeleteLeavesWithValueTest.java` | JUnit 6 tests |
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
