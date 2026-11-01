# 572. Subtree of Another Tree — v1: Same-tree check at every node

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Tree General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/)

## Problem

Return `true` if `subRoot` appears in `root` as a **subtree**: some node of `root` together with all its descendants is identical to
`subRoot`.

**Example**
```
root = [3,4,5,1,2], subRoot = [4,1,2]                       → true
root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] → false
```

**Constraints**
* `1 <= n <= 2000`; `1 <= m <= 1000`

## Approach: Same-tree check at every node

> Try every node of root as a starting point and compare the two trees exactly from there.

**Brute-force matching.** For each node of `root`, check `sameTree(node, subRoot)`.

* Time: **O(n·m)** — up to n starting points, each comparing up to m nodes.
* Space: **O(h)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0572/v1/SubtreeOfAnotherTree.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0572/v1/SubtreeOfAnotherTreeTest.java` | JUnit 6 tests |
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
