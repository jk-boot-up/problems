# 383. Ransom Note

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ransom-note/)

## Problem

Return `true` if `ransomNote` can be built from the letters of `magazine`, using each magazine letter at most once.

**Example 1**
```
Input:  ransomNote = "a", magazine = "b"
Output: false
```

**Example 2**
```
Input:  ransomNote = "aa", magazine = "aab"
Output: true
```

**Constraints**
* `1 <= ransomNote.length, magazine.length <= 10^5`; lowercase letters.

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Letter counts | `O(m + n)` | `O(1)` | [▶ animation](v1/animation/index.html) |

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
