# 779. K-th Symbol in Grammar — v1: Recursion on the parent

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Recursion &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/k-th-symbol-in-grammar/)

## Problem

Row 1 is `0`. Each next row replaces every `0` with `01` and every `1` with `10`. Return the `k`-th (1-indexed) symbol of row `n`.

**Example**
```
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
n = 2, k = 2 → 1;   n = 4, k = 5 → 1
```

**Constraints**
* `1 <= n <= 30`, `1 <= k <= 2^(n-1)`

## Approach: Recursion on the parent

> Look up the parent symbol in the row above; flip it if k is a right child.

**Recursion.** `kth(n, k)`: row 1 is 0. Otherwise the parent is `kth(n - 1, (k + 1) / 2)`; an odd `k` is a left child (same symbol), an
even `k` a right child (flipped).

* Time: **O(n)** — one call per row.
* Space: **O(n)** — recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0779/v1/KthSymbolInGrammar.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0779/v1/KthSymbolInGrammarTest.java` | JUnit 6 tests |
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

* [v2-parity-of-the-bits-of-k-1](../v2-parity-of-the-bits-of-k-1/README.md): Parity of the bits of k − 1 (`O(1)` time, `O(1)` space)
