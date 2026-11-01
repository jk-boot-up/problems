# 338. Counting Bits — v1: DP on i >> 1

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/counting-bits/)

## Problem

For every `i` in `0..n`, return the number of `1` bits in its binary representation.

**Example**
```
n = 5 → [0,1,1,2,1,2]
```

**Constraints**
* `0 <= n <= 10^5`

**Follow-up:** O(n) without a built-in bit count.

## Approach: DP on i >> 1

> bits(i) = bits(i >> 1) + (i & 1): drop the last bit, which you already counted, then add it back.

**Reuse smaller answers.** `i >> 1` is `i` without its last bit and is smaller than `i`, so `ans[i] = ans[i >> 1] + (i & 1)`.

* Time: **O(n)** — O(1) per number.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0338/v1/CountingBits.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0338/v1/CountingBitsTest.java` | JUnit 6 tests |
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
