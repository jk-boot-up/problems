# 258. Add Digits — v2: Digital root formula

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-digits/)

## Problem

Given a non-negative integer `num`, repeatedly add its digits until one digit remains, and return it.

**Example**
```
38 → 3 + 8 = 11 → 1 + 1 = 2
0  → 0
```

**Constraints**
* `0 <= num <= 2^31 - 1`

## Approach: Digital root formula

> A number and its digit sum leave the same remainder mod 9, so the answer is the digital root.

**Mod 9.** Since `10 ≡ 1 (mod 9)`, a number and its digit sum are congruent mod 9, and so is the final digit. That digit is between 1 and
9 for positive input, so it equals `1 + (num - 1) % 9`. Zero stays zero.

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0258/v2/AddDigits.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0258/v2/AddDigitsTest.java` | JUnit 6 tests |
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

* [v1-repeated-digit-sums](../v1-repeated-digit-sums/README.md): Repeated digit sums (`O(log n)` time, `O(1)` space)
