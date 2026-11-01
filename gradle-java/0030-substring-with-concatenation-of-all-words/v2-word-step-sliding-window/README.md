# 30. Substring with Concatenation of All Words — v2: Word-step sliding window

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

## Approach: Word-step sliding window

> All words share one length L, so slide a word-sized window for each of the L starting offsets, counting words in the window.

**Sliding window in word-sized steps.** Let `L` be the word length and `k` the number of words. For each offset `0..L-1`, slide
a window over `s` one word at a time, keeping a count of the words inside. If a word is not in `words`, reset the window. If a word
appears too often, drop words from the left until it doesn't. When the window holds `k` words, record its start.

* Time: **O(n·L)** — L offsets, each scanning about n / L words, and each word costs O(L) to cut out and hash.
* Space: **O(k)** — the two word-count maps.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0030/v2/SubstringConcatenation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0030/v2/SubstringConcatenationTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-check-every-start](../v1-check-every-start/README.md): Check every start (`O(n·k·L)` time, `O(k)` space)
