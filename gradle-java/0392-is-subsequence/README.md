# 392. Is Subsequence

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/is-subsequence/)

## Problem

Return `true` if `s` is a **subsequence** of `t`: that is, `s` can be formed by deleting some (possibly zero) characters
of `t` without changing the order of the rest.

**Example 1**
```
Input:  s = "abc", t = "ahbgdc"
Output: true
```

**Example 2**
```
Input:  s = "axc", t = "ahbgdc"
Output: false
```

**Constraints**
* `0 <= s.length <= 100`, `0 <= t.length <= 10^4`, lowercase letters only.

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(n)` | `O(1)` | [▶ animation](v1/animation/index.html) |

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
