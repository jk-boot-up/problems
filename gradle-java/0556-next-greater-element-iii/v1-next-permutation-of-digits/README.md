# 556. Next Greater Element III — v1: Next permutation of digits

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/next-greater-element-iii/)

## Problem

Return the smallest integer greater than `n` that uses exactly the same digits, or `-1` if none exists or it exceeds 32 bits.

**Example**
```
12 → 21,   21 → -1,   2147483486 → -1
```

**Constraints**
* `1 <= n <= 2^31 - 1`

## Approach: Next permutation of digits

> Apply next permutation to the digits; return -1 if there is none or it overflows 32 bits.

**Next permutation.** Find the rightmost digit smaller than its right neighbour, swap it with the smallest larger digit to its right,
reverse the tail. Parse as `long` and check the 32-bit limit.

* Time: **O(d)** — d ≤ 10 digits.
* Space: **O(d)** — the digit array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0556/v1/NextGreaterElementIII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0556/v1/NextGreaterElementIIITest.java` | JUnit 6 tests |
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
