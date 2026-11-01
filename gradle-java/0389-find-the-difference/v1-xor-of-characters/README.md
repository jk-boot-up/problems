# 389. Find the Difference — v1: XOR of characters

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-difference/)

## Problem

`t` is `s` shuffled with one extra letter added. Return that letter.

**Example**
```
s = "abcd", t = "abcde" → 'e',   s = "", t = "y" → 'y'
```

**Constraints**
* `0 <= s.length <= 1000`; `t.length == s.length + 1`

## Approach: XOR of characters

> XOR every character of both strings; all pairs cancel and the added letter remains.

**XOR.** Every letter of `s` appears in `t` too and cancels; the extra letter survives.

* Time: **O(n)** — one pass over each string.
* Space: **O(1)** — one accumulator.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0389/v1/FindTheDifference.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0389/v1/FindTheDifferenceTest.java` | JUnit 6 tests |
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
