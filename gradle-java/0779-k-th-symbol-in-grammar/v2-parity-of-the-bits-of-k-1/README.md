# 779. K-th Symbol in Grammar — v2: Parity of the bits of k − 1

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

## Approach: Parity of the bits of k − 1

> Each step right in the binary expansion of k − 1 flips the symbol, so the answer is the parity of its 1-bits.

**Parent chain.** Symbol `k-1` (0-indexed) of a row comes from symbol `(k-1)/2` of the row above: a left child copies its parent, a
right child flips it. Reading `k-1` in binary from the top, every 1-bit is a "right child" step and flips the symbol. So the answer is the
parity of the number of 1-bits in `k-1`; `n` does not matter.

* Time: **O(1)** — a bit count.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0779/v2/KthSymbolInGrammar.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0779/v2/KthSymbolInGrammarTest.java` | JUnit 6 tests |
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

* [v1-recursion-on-the-parent](../v1-recursion-on-the-parent/README.md): Recursion on the parent (`O(n)` time, `O(n)` space)
