# 131. Palindrome Partitioning — v1: Backtracking over prefixes

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindrome-partitioning/)

## Problem

Partition `s` so that every piece is a palindrome. Return all such partitions.

**Example**
```
"aab" → [["a","a","b"],["aa","b"]]
```

**Constraints**
* `1 <= s.length <= 16`; lowercase letters.

## Approach: Backtracking over prefixes

> Cut off a palindromic prefix, then partition the rest the same way.

**Backtracking.** From `start`, try every end `e` where `s[start..e]` is a palindrome (two-pointer check), add it to the path and recurse
from `e + 1`. Reaching the end records the path.

* Time: **O(n · 2ⁿ)** — up to 2ⁿ⁻¹ ways to cut, each checked in O(n).
* Space: **O(n)** — the recursion depth.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0131/v1/PalindromePartitioning.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0131/v1/PalindromePartitioningTest.java` | JUnit 6 tests |
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
