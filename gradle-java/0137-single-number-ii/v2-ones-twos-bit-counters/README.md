# 137. Single Number II — v2: Ones/twos bit counters

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/single-number-ii/)

## Problem

Every element appears **three times** except one, which appears exactly once. Find it in linear time and constant extra space.

**Example**
```
[2,2,3,2] → 3,   [0,1,0,1,0,1,99] → 99
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`

## Approach: Ones/twos bit counters

> Track, per bit, how many times it has been seen modulo 3 using two masks: ones and twos.

**A mod-3 counter for every bit.** `ones` holds bits seen 1 (mod 3) times, `twos` bits seen 2 times. For each `x`:
`ones = (ones ^ x) & ~twos`, then `twos = (twos ^ x) & ~ones`. A bit seen three times is cleared from both, so `ones` ends as the answer.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two ints.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0137/v2/SingleNumberII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0137/v2/SingleNumberIITest.java` | JUnit 6 tests |
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

* [v1-count-each-bit-position](../v1-count-each-bit-position/README.md): Count each bit position (`O(32·n)` time, `O(1)` space)
