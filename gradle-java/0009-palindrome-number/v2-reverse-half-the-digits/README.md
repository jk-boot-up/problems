# 9. Palindrome Number — v2: Reverse half the digits

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindrome-number/)

## Problem

Return `true` if the integer `x` reads the same forward and backward.

**Example**
```
121 → true,   -121 → false (reads 121-),   10 → false
```

**Constraints**
* `-2^31 <= x <= 2^31 - 1`

**Follow-up:** solve it without converting to a string.

## Approach: Reverse half the digits

> Reverse only the lower half of the digits and compare it with the upper half; no overflow, no strings.

**Half reversal.** Negative numbers and numbers ending in 0 (except 0) are not palindromes. Pop digits from `x` onto `rev` while
`x > rev`. Then `x == rev` (even length) or `x == rev / 10` (odd length, the middle digit sits in `rev`).

* Time: **O(log n)** — half of the digits are processed.
* Space: **O(1)** — two ints.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0009/v2/PalindromeNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0009/v2/PalindromeNumberTest.java` | JUnit 6 tests |
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

* [v1-compare-as-a-string](../v1-compare-as-a-string/README.md): Compare as a string (`O(log n)` time, `O(log n)` space)
