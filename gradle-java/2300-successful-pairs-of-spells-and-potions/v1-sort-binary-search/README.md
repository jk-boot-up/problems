# 2300. Successful Pairs of Spells and Potions — v1: Sort + binary search

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/)

## Problem

A spell and potion pair succeeds if `spell × potion >= success`. For each spell, return how many potions form a successful pair with it.

**Example**
```
spells = [5,1,3], potions = [1,2,3,4,5], success = 7 → [4,0,3]
```

**Constraints**
* `1 <= n, m <= 10^5`; `1 <= success <= 10^10`

## Approach: Sort + binary search

> Sort potions; for each spell, binary-search the weakest potion that still succeeds.

**Lower bound.** Sort potions. For a spell `s`, the smallest potion needed is `ceil(success / s)`; binary-search its position; every potion
from there on works. Use `long` arithmetic.

* Time: **O((n + m) log m)** — sort plus one search per spell.
* Space: **O(m)** — the sorted copy.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p2300/v1/SuccessfulPairs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p2300/v1/SuccessfulPairsTest.java` | JUnit 6 tests |
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
