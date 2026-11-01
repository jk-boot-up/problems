# 1047. Remove All Adjacent Duplicates In String — v1: Stack via StringBuilder

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

## Problem

Repeatedly remove two adjacent equal letters from `s` until no such pair remains. Return the final string (it is unique).

**Example**
```
"abbaca" → "ca",   "azxxzy" → "ay"
```

**Constraints**
* `1 <= s.length <= 10^5`

## Approach: Stack via StringBuilder

> Use the result as a stack: a letter equal to the top cancels it, otherwise it is pushed.

**Stack.** For each letter: if it equals the last kept letter, delete that letter; otherwise append it.

* Time: **O(n)** — O(1) per letter.
* Space: **O(n)** — the builder.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1047/v1/RemoveAdjacentDuplicates.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1047/v1/RemoveAdjacentDuplicatesTest.java` | JUnit 6 tests |
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
