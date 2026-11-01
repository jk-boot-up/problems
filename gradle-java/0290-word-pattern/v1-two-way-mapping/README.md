# 290. Word Pattern — v1: Two-way mapping

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-pattern/)

## Problem

Given a `pattern` of letters and a string `s` of space-separated words, return `true` if `s` **follows** the pattern: there is a
one-to-one correspondence between pattern letters and words.

**Example 1**
```
Input:  pattern = "abba", s = "dog cat cat dog"
Output: true
```

**Example 2**
```
Input:  pattern = "abba", s = "dog cat cat fish"
Output: false
```

**Example 3**
```
Input:  pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

**Constraints**
* `1 <= pattern.length <= 300`; `1 <= s.length <= 3000`; words are lowercase and separated by single spaces.

## Approach: Two-way mapping

> Each pattern letter must map to exactly one word and each word to exactly one letter.

**Bijection check.** Split `s` into words; if the counts differ, return `false`. Walk both together with two maps
(letter → word and word → letter); any conflict means the pattern is not followed.

* Time: **O(n)** — n is the length of s; each word is hashed once.
* Space: **O(n)** — the maps hold the distinct words.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0290/v1/WordPattern.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0290/v1/WordPatternTest.java` | JUnit 6 tests |
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
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
