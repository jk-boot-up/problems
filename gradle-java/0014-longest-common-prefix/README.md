# 14. Longest Common Prefix

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-common-prefix/)

## Problem

Return the longest common prefix shared by all strings in `strs`, or `""` if there is none.

**Example 1**
```
Input:  strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2**
```
Input:  strs = ["dog","racecar","car"]
Output: ""
```

**Constraints**
* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`, lowercase English letters

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(S)` | `O(1)` | [▶ animation](v1/animation/index.html) |

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
