# 76. Minimum Window Substring — v1: Sliding window with counts

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-window-substring/)

## Problem

Given strings `s` and `t`, return the **shortest substring** of `s` that contains every character of `t` (including duplicates).
Return `""` if there is none. The answer is unique when it exists.

**Example 1**
```
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Example 2**
```
Input:  s = "a", t = "a"
Output: "a"
```

**Example 3**
```
Input:  s = "a", t = "aa"
Output: ""
```

**Constraints**
* `1 <= s.length, t.length <= 10^5`; upper- and lower-case letters.

## Approach: Sliding window with counts

> Expand right until the window covers t, then shrink left as far as it stays covering; remember the smallest.

**Sliding window.** `need[c]` counts what `t` still needs; `missing` is how many characters are still missing.
Move `right`: if `need[s[right]] > 0`, it fills a gap (`missing--`); decrement `need` either way. When `missing == 0`, shrink from
the left while `need[s[left]] < 0` (that character is in surplus), record the window, then give up `s[left]` to keep searching.

* Time: **O(m + n)** — each pointer passes over s once, plus one pass over t.
* Space: **O(1)** — a fixed 128-entry count array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0076/v1/MinimumWindowSubstring.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0076/v1/MinimumWindowSubstringTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
