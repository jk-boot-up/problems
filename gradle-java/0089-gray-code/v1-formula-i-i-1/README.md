# 89. Gray Code — v1: Formula i ^ (i >> 1)

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/gray-code/)

## Problem

Return any `n`-bit Gray code sequence: `2^n` integers starting at 0, each appearing once, where consecutive values (and the last and first)
differ in exactly one bit.

**Example**
```
n = 2 → [0,1,3,2],   n = 1 → [0,1]
```

**Constraints**
* `1 <= n <= 16`

## Approach: Formula i ^ (i >> 1)

> The i-th Gray code is i XOR (i >> 1); consecutive codes differ in exactly one bit.

**Binary-reflected Gray code.** `g(i) = i ^ (i >> 1)`. Going from `i` to `i + 1` flips a run of low bits; the XOR with the shifted value
cancels all but one of those flips.

* Time: **O(2ⁿ)** — one formula per code.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0089/v1/GrayCode.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0089/v1/GrayCodeTest.java` | JUnit 6 tests |
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
