# 30. Substring with Concatenation of All Words — v1: Check every start

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

## Approach: Check every start

> For each start index, cut k words and compare their counts with the required counts.

**Brute force.** For each start `i` with room for `k` words, read the `k` consecutive chunks of length `L` and count them;
stop early when a chunk is not needed or is seen too often.

* Time: **O(n·k·L)** — n starts × k words × L characters to cut each word.
* Space: **O(k)** — the per-start count map.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0030/v1/SubstringConcatenation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0030/v1/SubstringConcatenationTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-word-step-sliding-window](../v2-word-step-sliding-window/README.md): Word-step sliding window (`O(n·L)` time, `O(k)` space)
