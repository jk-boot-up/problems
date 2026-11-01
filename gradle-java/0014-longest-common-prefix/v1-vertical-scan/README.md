# 14. Longest Common Prefix — v1: Vertical scan

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-common-prefix/)

## Problem

Return the longest common prefix shared by all strings in `strs`, or `""` if there is none.

**Example 1**
```
Input:  strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2**
```
Input:  strs = ["dog","racecar","car"]
Output: ""
```

**Constraints**
* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`, lowercase English letters

## Approach: Vertical scan

> Compare column by column: the prefix grows until some string ends or differs in that column.

**Vertical scan.** For column `c = 0, 1, …`, check that every string has a character at `c` equal to `strs[0].charAt(c)`.
Stop at the first mismatch or end of a string; the prefix is `strs[0].substring(0, c)`.

* Time: **O(S)** — S is the total number of characters; each is compared at most once.
* Space: **O(1)** — apart from the returned substring.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0014/v1/LongestCommonPrefix.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0014/v1/LongestCommonPrefixTest.java` | JUnit 6 tests |
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
