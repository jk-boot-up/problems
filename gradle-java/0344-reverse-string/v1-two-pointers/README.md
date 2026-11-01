# 344. Reverse String — v1: Two pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-string/)

## Problem

Reverse an array of characters `s` **in place** with O(1) extra memory.

**Example**
```
["h","e","l","l","o"] → ["o","l","l","e","h"]
```

**Constraints**
* `1 <= s.length <= 10^5`

## Approach: Two pointers

> Swap the outermost pair and move both pointers inward.

**Swap ends.** `l = 0`, `r = n - 1`; swap and move inward until they meet.

* Time: **O(n)** — n/2 swaps.
* Space: **O(1)** — one temporary.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0344/v1/ReverseString.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0344/v1/ReverseStringTest.java` | JUnit 6 tests |
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
