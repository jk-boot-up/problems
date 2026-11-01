# 3. Longest Substring Without Repeating Characters — v1: Window with a hash set

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

## Approach: Window with a hash set

> Grow the window on the right; while the new character is already inside, shrink from the left.

**Sliding window with a set.** The set holds the window's characters. Before adding `s[right]`, remove `s[left]` and advance
`left` until `s[right]` is no longer in the set.

* Time: **O(n)** — each character is added once and removed at most once.
* Space: **O(k)** — the set holds at most k distinct characters.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0003/v1/LongestSubstring.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0003/v1/LongestSubstringTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-window-with-last-seen-index](../v2-window-with-last-seen-index/README.md): Window with last-seen index (`O(n)` time, `O(k)` space)
