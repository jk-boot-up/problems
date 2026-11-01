# 140. Word Break II — v1: Memoized backtracking

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-break-ii/)

## Problem

Return every way to split `s` into a space-separated sentence of dictionary words (words may be reused), in any order.

**Example**
```
s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"] → ["cats and dog","cat sand dog"]
s = "catsandog", same dict → []
```

**Constraints**
* `1 <= s.length <= 20`

## Approach: Memoized backtracking

> Backtrack over dictionary-word prefixes, memoizing all sentences for each suffix.

**Memo on the start index.** `sentences(i)` lists all sentences for `s[i..]`: for each dictionary word that starts at `i`, prepend it to every
sentence of the remainder. Cache results per index in a `MyHashMap`.

* Time: **O(2ⁿ)** — the number of sentences itself can be exponential.
* Space: **O(2ⁿ)** — the memoized sentences.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0140/v1/WordBreakII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0140/v1/WordBreakIITest.java` | JUnit 6 tests |
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
