# 151. Reverse Words in a String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/)

## Problem

Given a string `s`, reverse the order of its **words**. A word is a run of non-space characters. The result must have exactly
one space between words and no leading or trailing spaces, even if `s` has extra spaces.

**Example 1**
```
Input:  s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2**
```
Input:  s = "  hello world  "
Output: "world hello"
```

**Example 3**
```
Input:  s = "a good   example"
Output: "example good a"
```

**Constraints**
* `1 <= s.length <= 10^4`; letters, digits and spaces; at least one word.

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Split, reverse, join | `O(n)` | `O(n)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Manual right-to-left scan | `O(n)` | `O(n)` | [▶ animation](v2/animation/index.html) |

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
