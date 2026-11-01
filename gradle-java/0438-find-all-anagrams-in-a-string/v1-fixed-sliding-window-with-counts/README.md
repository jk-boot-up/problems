# 438. Find All Anagrams in a String — v1: Fixed sliding window with counts

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

## Problem

Return the start indices of all substrings of `s` that are anagrams of `p`, in any order.

**Example**
```
s = "cbaebabacd", p = "abc" → [0,6]
s = "abab", p = "ab"        → [0,1,2]
```

**Constraints**
* `1 <= s.length, p.length <= 3 * 10^4`; lowercase letters.

## Approach: Fixed sliding window with counts

> Slide a window of length |p| and keep letter counts; a window is an anagram when every count matches.

**Counts + mismatch counter.** `need[c]` is `count_p(c) - count_window(c)`; `diff` is the number of letters with `need != 0`. Adding or
removing a letter changes one count and updates `diff` in O(1). A window with `diff == 0` is an anagram.

* Time: **O(n)** — each letter enters and leaves the window once.
* Space: **O(1)** — 26 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0438/v1/FindAllAnagrams.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0438/v1/FindAllAnagramsTest.java` | JUnit 6 tests |
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
