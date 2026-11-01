# 67. Add Binary — v1: Right-to-left with carry

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-binary/)

## Problem

Given two binary strings `a` and `b`, return their sum as a binary string.

**Example**
```
a = "11",   b = "1"    → "100"
a = "1010", b = "1011" → "10101"
```

**Constraints**
* `1 <= a.length, b.length <= 10^4`; no leading zeros except "0" itself.

## Approach: Right-to-left with carry

> Add digit by digit from the right with a carry, exactly like on paper.

**Schoolbook addition.** Walk both strings from the end; `sum = carry + bitA + bitB`; append `sum % 2`, carry `sum / 2`. Reverse at the end.

* Time: **O(max(m, n))** — one step per digit.
* Space: **O(max(m, n))** — the result builder.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0067/v1/AddBinary.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0067/v1/AddBinaryTest.java` | JUnit 6 tests |
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
