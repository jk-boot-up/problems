# 844. Backspace String Compare — v1: Backward two pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/backspace-string-compare/)

## Problem

`#` is a backspace. Return `true` if `s` and `t` are equal after typing both into empty editors.

**Example**
```
"ab#c", "ad#c" → true,   "ab##", "c#d#" → true,   "a#c", "b" → false
```

**Constraints**
* `1 <= s.length, t.length <= 200`

**Follow-up:** O(n) time and O(1) space.

## Approach: Backward two pointers

> Walk both strings from the end, skipping characters erased by '#', and compare the survivors one by one.

**From the back.** For each string, find the next surviving character from the right by counting pending backspaces. Compare surviving
characters pairwise.

* Time: **O(m + n)** — each character once.
* Space: **O(1)** — a few indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0844/v1/BackspaceStringCompare.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0844/v1/BackspaceStringCompareTest.java` | JUnit 6 tests |
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
