# 404. Sum of Left Leaves — v1: DFS with an is-left flag

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree DFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sum-of-left-leaves/)

## Problem

Return the sum of all **left leaves**: leaves that are the left child of their parent.

**Example**
```
[3,9,20,null,null,15,7] → 24   (9 + 15)
[1]                     → 0
```

**Constraints**
* `1 <= n <= 1000`

## Approach: DFS with an is-left flag

> A node is a left leaf when it is a parent's left child and has no children; pass that flag down.

**DFS.** Recurse with a flag saying whether the node is a left child. A leaf contributes its value only when the flag is set.

* Time: **O(n)**.
* Space: **O(h)** — recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0404/v1/SumOfLeftLeaves.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0404/v1/SumOfLeftLeavesTest.java` | JUnit 6 tests |
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
