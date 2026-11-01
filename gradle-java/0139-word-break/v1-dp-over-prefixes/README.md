# 139. Word Break — v1: DP over prefixes

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** 1D DP &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/word-break/)

## Problem

Return `true` if `s` can be split into a sequence of one or more words from `wordDict` (words may be reused).

**Example**
```
s = "leetcode", wordDict = ["leet","code"]            → true
s = "applepenapple", wordDict = ["apple","pen"]       → true
s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] → false
```

**Constraints**
* `1 <= s.length <= 300`; `1 <= wordDict.length <= 1000`; `1 <= wordDict[i].length <= 20`

## Approach: DP over prefixes

> ok[i] is true when the first i characters split into words: some earlier ok[j] plus a dictionary word s[j..i).

**Prefix DP.** `ok[0] = true`. For each end `i`, look back at most `maxLen` characters: `ok[i]` is true if some `ok[j]` is true and
`s.substring(j, i)` is in the dictionary (a `MyHashSet`).

* Time: **O(n · L²)** — n ends × up to L starts × O(L) substring hashing (L = longest word).
* Space: **O(n + D)** — the dp array and the dictionary set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0139/v1/WordBreak.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0139/v1/WordBreakTest.java` | JUnit 6 tests |
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
