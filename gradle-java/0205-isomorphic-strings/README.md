# 205. Isomorphic Strings

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

## Solutions

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Two-way mapping | `O(n)` | `O(1)` | [▶ animation](v1/animation/index.html) |

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
