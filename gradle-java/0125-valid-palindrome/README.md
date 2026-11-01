# 125. Valid Palindrome

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-palindrome/)

## Problem

A phrase is a **palindrome** if, after lower-casing it and removing every non-alphanumeric character, it reads the same
forward and backward. Return `true` if `s` is a palindrome.

**Example 1**
```
Input:  s = "A man, a plan, a canal: Panama"
Output: true
```

**Example 2**
```
Input:  s = "race a car"
Output: false
```

**Example 3**
```
Input:  s = " "
Output: true
```

**Constraints**
* `1 <= s.length <= 2 * 10^5`, printable ASCII.

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
