# 881. Boats to Save People — v1: Sort + two pointers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/boats-to-save-people/)

## Problem

Each boat carries at most two people with total weight at most `limit` (every person weighs at most `limit`). Return the minimum number of
boats.

**Example**
```
people = [1,2], limit = 3 → 1,   [3,2,2,1], limit = 3 → 3,   [3,5,3,4], limit = 5 → 4
```

**Constraints**
* `1 <= people.length <= 5 * 10^4`

## Approach: Sort + two pointers

> Sort; the heaviest person shares a boat with the lightest if they fit, otherwise goes alone.

**Greedy pairing.** Sort. The heaviest person needs a boat anyway; if the lightest fits too, they share. Move the pointers inward.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0881/v1/BoatsToSavePeople.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0881/v1/BoatsToSavePeopleTest.java` | JUnit 6 tests |
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
