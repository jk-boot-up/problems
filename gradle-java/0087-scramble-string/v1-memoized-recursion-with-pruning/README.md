# 87. Scramble String — v1: Memoized recursion with pruning

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Multidimensional DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/scramble-string/)

## Problem

A string is scrambled by splitting it into two non-empty parts, optionally swapping them, and scrambling each part recursively. Return
`true` if `s2` is a scrambled string of `s1`.

**Example**
```
"great", "rgeat" → true,   "abcde", "caebd" → false,   "a", "a" → true
```

**Constraints**
* `1 <= s1.length <= 30`; `s2.length == s1.length`

## Approach: Memoized recursion with pruning

> s2 is a scramble of s1 if some split of s1 matches s2's halves either in order or swapped, recursively.

**Recursion + memo.** `scr(a, b)`: equal strings are true; different letter counts are false. Otherwise try every split length `k`:
(`a[..k]` ~ `b[..k]` and `a[k..]` ~ `b[k..]`) or (`a[..k]` ~ `b[n-k..]` and `a[k..]` ~ `b[..n-k]`). Memoize on `(a, b)` in a `MyHashMap`.

* Time: **O(n⁴)** — O(n³) distinct substring pairs, each trying O(n) splits.
* Space: **O(n³)** — the memo.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0087/v1/ScrambleString.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0087/v1/ScrambleStringTest.java` | JUnit 6 tests |
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
