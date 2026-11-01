# 342. Power of Four — v1: Single bit at an even position

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/power-of-four/)

## Problem

Return `true` if `n` is a power of four.

**Example**
```
16 → true
5  → false
1  → true
```

**Constraints**
* `-2^31 <= n <= 2^31 - 1`

## Approach: Single bit at an even position

> A power of four is a power of two whose single 1-bit sits at an even position.

**Two bit tests.** `n > 0 && (n & (n - 1)) == 0` checks for a single 1-bit. Powers of four have it at bit 0, 2, 4, …, so it must also
overlap the mask `0x55555555` (binary `…0101`).

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0342/v1/PowerOfFour.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0342/v1/PowerOfFourTest.java` | JUnit 6 tests |
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
