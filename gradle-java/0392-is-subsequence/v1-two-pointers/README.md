# 392. Is Subsequence — v1: Two pointers

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

## Approach: Two pointers

> Walk through t once; advance the pointer in s each time its current character appears.

**Two pointers.** `i` walks `s`, `j` walks `t`. Whenever `s[i] == t[j]`, advance `i`. Always advance `j`.
`s` is a subsequence if `i` reaches `s.length()`.

* Time: **O(n)** — n is the length of t; each character of t is checked once.
* Space: **O(1)** — two indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0392/v1/IsSubsequence.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0392/v1/IsSubsequenceTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
