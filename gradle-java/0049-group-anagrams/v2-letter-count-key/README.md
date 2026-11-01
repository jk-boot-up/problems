# 49. Group Anagrams — v2: Letter-count key

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/group-anagrams/)

## Problem

Group the strings in `strs` so that anagrams are together. Return the groups in any order.

**Example 1**
```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Example 2**
```
Input:  strs = [""]
Output: [[""]]
```

**Constraints**
* `1 <= strs.length <= 10^4`, `0 <= strs[i].length <= 100`; lowercase letters.

## Approach: Letter-count key

> Give every word a key that is identical for all its anagrams, and group words by key.

**Count signature.** Build a key from the 26 letter counts (e.g. `"1#0#0#...#1"`). Anagrams share the same counts, so they share a key.
Collect words in a `Map<String, List<String>>`.

* Time: **O(n·k)** — n words of length up to k; each key takes O(k + 26).
* Space: **O(n·k)** — the map stores every word.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0049/v2/GroupAnagrams.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0049/v2/GroupAnagramsTest.java` | JUnit 6 tests |
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

* [v1-sorted-word-key](../v1-sorted-word-key/README.md): Sorted-word key (`O(n·k log k)` time, `O(n·k)` space)
