# 190. Reverse Bits — v2: Bit-by-bit shifting

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-bits/)

## Problem

Reverse the bits of a 32-bit **unsigned** integer (in Java it arrives in an `int`, so the top bit may be the sign bit).

**Example**
```
Input:  00000010100101000001111010011100   (43261596)
Output: 00111001011110000010100101000000   (964176192)
```

**Constraints**
* The input is a 32-bit binary value.

**Follow-up:** if called many times, how would you optimize it?

## Approach: Bit-by-bit shifting

> Shift bits out of n from the right and into the result from the left, 32 times.

**Shift and build.** 32 times: shift `result` left, add `n & 1`, then shift `n` right with `>>>` (unsigned).

* Time: **O(1)** — always 32 iterations.
* Space: **O(1)** — one int.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0190/v2/ReverseBits.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0190/v2/ReverseBitsTest.java` | JUnit 6 tests |
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

* [v1-swap-halves-divide-and-conquer](../v1-swap-halves-divide-and-conquer/README.md): Swap halves (divide and conquer) (`O(1)` time, `O(1)` space)
