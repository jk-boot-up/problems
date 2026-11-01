# 3. Longest Substring Without Repeating Characters — v2: Window with last-seen index

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem

Given a string `s`, return the length of the longest **substring** (contiguous) that contains no repeated characters.

**Example 1**
```
Input:  s = "abcabcbb"
Output: 3   ("abc")
```

**Example 2**
```
Input:  s = "bbbbb"
Output: 1
```

**Example 3**
```
Input:  s = "pwwkew"
Output: 3   ("wke"; "pwke" is a subsequence, not a substring)
```

**Constraints**
* `0 <= s.length <= 5 * 10^4`; letters, digits, symbols and spaces.

## Approach: Window with last-seen index

> Keep a window with no repeats; when a character repeats, jump the left edge just past its previous position.

**Sliding window with last positions.** Store the last index of every character. Move `right` across the string; if `s[right]`
was last seen at or after `left`, jump `left` to one past that position. The window `left..right` never contains a repeat.

* Time: **O(n)** — each character is processed once; left only jumps forward.
* Space: **O(k)** — k is the alphabet size (here a fixed array of 128 entries).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0003/v2/LongestSubstring.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0003/v2/LongestSubstringTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-window-with-a-hash-set](../v1-window-with-a-hash-set/README.md): Window with a hash set (`O(n)` time, `O(k)` space)
