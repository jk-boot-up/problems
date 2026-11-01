# 567. Permutation in String — v1: Fixed window with counts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/permutation-in-string/)

## Problem

Return `true` if `s2` contains a permutation of `s1` as a substring.

**Example**
```
s1 = "ab", s2 = "eidbaooo" → true ("ba"),   s1 = "ab", s2 = "eidboaoo" → false
```

**Constraints**
* `1 <= s1.length, s2.length <= 10^4`; lowercase letters.

## Approach: Fixed window with counts

> Slide a window of length |s1| over s2; a permutation exists when the window's letter counts equal s1's.

**Counts + matches.** Keep `need[26]` (s1 minus window) and `zero` = how many letters currently have `need == 0`. Each letter entering or
leaving the window updates one count and `zero` in O(1); `zero == 26` means the window is a permutation.

* Time: **O(n)** — n = |s2|.
* Space: **O(1)** — 26 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0567/v1/PermutationInString.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0567/v1/PermutationInStringTest.java` | JUnit 6 tests |
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
