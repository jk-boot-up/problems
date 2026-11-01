# 95. Unique Binary Search Trees II — v1: Recursive generation

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-binary-search-trees-ii/)

## Problem

Return all structurally unique BSTs that store exactly the values `1..n`, in any order.

**Example**
```
n = 3 → 5 trees: [1,null,2,null,3], [1,null,3,2], [2,1,3], [3,1,null,null,2], [3,2,null,1]
```

**Constraints**
* `1 <= n <= 8`

## Approach: Recursive generation

> For each root r, combine every left tree built from smaller values with every right tree built from larger ones.

**Divide by the root.** `build(lo, hi)` returns all BSTs of `lo..hi`: for each root `r`, pair every tree of `build(lo, r-1)` with every tree of
`build(r+1, hi)` (subtrees are shared between results, which is fine because they are never modified).

* Time: **O(n · Cₙ)** — Cₙ (the n-th Catalan number) trees, each assembled with O(n) work.
* Space: **O(n · Cₙ)** — the trees produced.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0095/v1/UniqueBSTsII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0095/v1/UniqueBSTsIITest.java` | JUnit 6 tests |
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
