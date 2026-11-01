# 771. Jewels and Stones — v1: Lookup table

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/jewels-and-stones/)

## Problem

`jewels` lists the letter types that are jewels; `stones` lists your stones. Return how many of your stones are jewels (case-sensitive).

**Example**
```
jewels = "aA", stones = "aAAbbbb" → 3,   jewels = "z", stones = "ZZ" → 0
```

**Constraints**
* `1 <= jewels.length, stones.length <= 50`; letters only.

## Approach: Lookup table

> Mark the jewel letters in a lookup table, then count stones that are marked.

**Boolean table.** `isJewel[128]` marks each jewel letter; count stones with a mark.

* Time: **O(j + s)** — two passes.
* Space: **O(1)** — 128 flags.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0771/v1/JewelsAndStones.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0771/v1/JewelsAndStonesTest.java` | JUnit 6 tests |
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
