# 76. Minimum Window Substring

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

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Sliding window with counts | `O(m + n)` | `O(1)` | [▶ animation](v1/animation/index.html) |

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
