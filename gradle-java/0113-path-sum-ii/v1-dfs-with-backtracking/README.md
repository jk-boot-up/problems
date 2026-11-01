# 113. Path Sum II — v1: DFS with backtracking

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/path-sum-ii/)

## Problem

Return every **root-to-leaf** path whose node values add up to `targetSum`, each as a list of values.

**Example**
```
root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
→ [[5,4,11,2],[5,8,4,5]]
```

**Constraints**
* `0 <= n <= 5000`

## Approach: DFS with backtracking

> DFS with a running path; at each leaf whose remaining sum is zero, copy the path into the answer.

**Backtracking.** Push the node onto the path and subtract its value. At a leaf with remaining 0, record a copy. Recurse into children,
then pop the node.

* Time: **O(n · h)** — each node is visited once; copying a path costs O(h).
* Space: **O(h)** — the path and the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0113/v1/PathSumII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0113/v1/PathSumIITest.java` | JUnit 6 tests |
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
