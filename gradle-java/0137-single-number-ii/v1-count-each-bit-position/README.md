# 137. Single Number II — v1: Count each bit position

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/single-number-ii/)

## Problem

Every element appears **three times** except one, which appears exactly once. Find it in linear time and constant extra space.

**Example**
```
[2,2,3,2] → 3,   [0,1,0,1,0,1,99] → 99
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`

## Approach: Count each bit position

> For each of the 32 bits, count how many numbers have it set; counts not divisible by 3 belong to the single number.

**Per-bit sums.** For `bit = 0..31`, sum `(x >> bit) & 1` over all numbers; if the sum mod 3 is 1, set that bit in the answer.

* Time: **O(32·n)** — 32 passes, which is O(n).
* Space: **O(1)** — counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0137/v1/SingleNumberII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0137/v1/SingleNumberIITest.java` | JUnit 6 tests |
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

* [v2-ones-twos-bit-counters](../v2-ones-twos-bit-counters/README.md): Ones/twos bit counters (`O(n)` time, `O(1)` space)
