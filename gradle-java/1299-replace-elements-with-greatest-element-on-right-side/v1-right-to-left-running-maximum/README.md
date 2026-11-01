# 1299. Replace Elements with Greatest Element on Right Side — v1: Right-to-left running maximum

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)

## Problem

Replace every element with the greatest element to its right, and the last element with `-1`.

**Example**
```
[17,18,5,4,6,1] → [18,6,6,6,1,-1],   [400] → [-1]
```

**Constraints**
* `1 <= arr.length <= 10^4`

## Approach: Right-to-left running maximum

> Walk from the right, carrying the maximum seen so far.

**Suffix maximum.** Start with `max = -1`; going right to left, store `max` in the slot, then update `max` with the old value.

* Time: **O(n)** — one pass.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1299/v1/ReplaceWithGreatestOnRight.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1299/v1/ReplaceWithGreatestOnRightTest.java` | JUnit 6 tests |
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
