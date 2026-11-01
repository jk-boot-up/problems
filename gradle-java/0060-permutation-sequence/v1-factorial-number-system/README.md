# 60. Permutation Sequence — v1: Factorial number system

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/permutation-sequence/)

## Problem

The permutations of `1..n`, listed in lexicographic order, are numbered from 1. Return the `k`-th one as a string.

**Example**
```
n = 3, k = 3 → "213",   n = 4, k = 9 → "2314",   n = 3, k = 1 → "123"
```

**Constraints**
* `1 <= n <= 9`; `1 <= k <= n!`

## Approach: Factorial number system

> Factorials tell how many permutations start with each digit; pick digits one by one with k's factorial-base digits.

**Skip whole blocks.** With `m` digits left, each choice of first digit starts a block of `(m-1)!` permutations. Using zero-based `k`, the
block index is `k / (m-1)!`: take that remaining digit, set `k %= (m-1)!`, and repeat.

* Time: **O(n²)** — n picks, each removing from a list of up to n digits.
* Space: **O(n)** — the remaining digits.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0060/v1/PermutationSequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0060/v1/PermutationSequenceTest.java` | JUnit 6 tests |
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
