# 112. Path Sum — v1: Recursive DFS

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-sum/)

## Problem

Return `true` if the tree has a **root-to-leaf** path whose values add up to `targetSum`. A leaf has no children.

**Example 1**
```
Input:  root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true   (5 → 4 → 11 → 2)
```

**Example 2**
```
Input:  root = [1,2,3], targetSum = 5
Output: false
```

**Constraints**
* `0 <= n <= 5000`; `-1000 <= Node.val, targetSum <= 1000`

## Approach: Recursive DFS

> Subtract each node's value from the target on the way down; a leaf must leave exactly zero.

**Remaining sum.** At each node subtract its value. At a leaf, check whether the remainder is 0. Otherwise ask either child.

* Time: **O(n)** — each node is visited at most once.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0112/v1/PathSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0112/v1/PathSumTest.java` | JUnit 6 tests |
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
