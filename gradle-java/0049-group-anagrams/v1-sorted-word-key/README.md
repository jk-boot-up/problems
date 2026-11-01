# 49. Group Anagrams — v1: Sorted-word key

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

## Approach: Sorted-word key

> Sorting a word's letters gives the same key for all of its anagrams.

**Sort each word.** The key is the word with its letters sorted, e.g. `"eat" → "aet"`.

* Time: **O(n·k log k)** — sorting each of n words of length k.
* Space: **O(n·k)** — the map stores every word.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0049/v1/GroupAnagrams.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0049/v1/GroupAnagramsTest.java` | JUnit 6 tests |
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

* [v2-letter-count-key](../v2-letter-count-key/README.md): Letter-count key (`O(n·k)` time, `O(n·k)` space)
