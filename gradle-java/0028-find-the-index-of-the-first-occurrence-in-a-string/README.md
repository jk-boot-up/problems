# 28. Find the Index of the First Occurrence in a String

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Problem

Return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` does not occur.

**Example 1**
```
Input:  haystack = "sadbutsad", needle = "sad"
Output: 0
```

**Example 2**
```
Input:  haystack = "leetcode", needle = "leeto"
Output: -1
```

**Constraints**
* `1 <= haystack.length, needle.length <= 10^4`, lowercase letters only.

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Brute force | `O(n·m)` | `O(1)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | KMP | `O(n + m)` | `O(m)` | [▶ animation](v2/animation/index.html) |

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
