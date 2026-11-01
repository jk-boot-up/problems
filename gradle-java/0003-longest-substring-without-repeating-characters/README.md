# 3. Longest Substring Without Repeating Characters

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

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Window with a hash set | `O(n)` | `O(k)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Window with last-seen index | `O(n)` | `O(k)` | [▶ animation](v2/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
