# 30. Substring with Concatenation of All Words

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

## Problem

You are given a string `s` and an array `words` of strings that all have the **same length**. A *concatenated substring* is a
substring of `s` made of every word in `words` exactly once, in any order. Return the starting indices of all concatenated
substrings in `s`, in any order.

**Example 1**
```
Input:  s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
```

**Example 2**
```
Input:  s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
```

**Example 3**
```
Input:  s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
```

**Constraints**
* `1 <= s.length <= 10^4`, `1 <= words.length <= 5000`, `1 <= words[i].length <= 30`

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Check every start | `O(n·k·L)` | `O(k)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Word-step sliding window | `O(n·L)` | `O(k)` | [▶ animation](v2/animation/index.html) |

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
