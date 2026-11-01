# 205. Isomorphic Strings — v1: Two-way mapping

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/isomorphic-strings/)

## Problem

Two strings `s` and `t` are **isomorphic** if the characters of `s` can be replaced to get `t`: every occurrence of a character
is replaced by the same character, and no two different characters map to the same character (a character may map to itself).

**Example 1**
```
Input:  s = "egg", t = "add"
Output: true
```

**Example 2**
```
Input:  s = "foo", t = "bar"
Output: false
```

**Example 3**
```
Input:  s = "paper", t = "title"
Output: true
```

**Constraints**
* `1 <= s.length <= 5 * 10^4`, `t.length == s.length`; any ASCII characters.

## Approach: Two-way mapping

> Map characters both ways (s→t and t→s); any conflicting mapping means not isomorphic.

**Two maps.** Walk both strings together. If `s[i]` already maps to something other than `t[i]`, or `t[i]` is already the image
of a different character, return `false`. Otherwise record both directions.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two arrays of 256 entries.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0205/v1/IsomorphicStrings.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0205/v1/IsomorphicStringsTest.java` | JUnit 6 tests |
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
