# 96. Unique Binary Search Trees — v1: Catalan DP

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/unique-binary-search-trees/)

## Problem

Return the number of structurally unique BSTs that store exactly the values `1..n`.

**Example**
```
n = 3 → 5,   n = 1 → 1
```

**Constraints**
* `1 <= n <= 19`

## Approach: Catalan DP

> Choosing root r splits 1..n into r−1 left values and n−r right values: G(n) = Σ G(r−1)·G(n−r) (Catalan numbers).

**DP over sizes.** `G(0) = G(1) = 1`. For each size `k`, sum over every root `r`: the left subtree holds `r - 1` values and the right
`k - r`, and any left shape combines with any right shape.

* Time: **O(n²)** — n sizes × up to n roots.
* Space: **O(n)** — the G array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0096/v1/UniqueBSTs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0096/v1/UniqueBSTsTest.java` | JUnit 6 tests |
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
