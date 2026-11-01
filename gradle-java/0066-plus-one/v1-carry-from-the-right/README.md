# 66. Plus One — v1: Carry from the right

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/plus-one/)

## Problem

A large integer is given as an array of `digits` (most significant first, no leading zeros). Add one and return the resulting digits.

**Example**
```
[1,2,3] → [1,2,4],   [4,3,2,1] → [4,3,2,2],   [9] → [1,0]
```

**Constraints**
* `1 <= digits.length <= 100`; `0 <= digits[i] <= 9`

## Approach: Carry from the right

> Add one from the right: 9s turn into 0s and carry; the first non-9 just increments.

**Right-to-left.** From the last digit: if it is below 9, increment and return. Otherwise set it to 0 and continue left. If every digit
was 9, the answer is `1` followed by zeros.

* Time: **O(n)** — at most one pass.
* Space: **O(1)** — in place, except when a new leading digit is needed.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0066/v1/PlusOne.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0066/v1/PlusOneTest.java` | JUnit 6 tests |
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
