# 242. Valid Anagram — v2: Letter counts

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-anagram/)

## Problem

Return `true` if `t` is an **anagram** of `s`: it uses exactly the same letters, the same number of times, in any order.

**Example 1**
```
Input:  s = "anagram", t = "nagaram"
Output: true
```

**Example 2**
```
Input:  s = "rat", t = "car"
Output: false
```

**Constraints**
* `1 <= s.length, t.length <= 5 * 10^4`; lowercase letters.

**Follow-up:** what if the inputs contain Unicode characters? (Use a hash map instead of a fixed array.)

## Approach: Letter counts

> Two strings are anagrams exactly when every letter appears the same number of times in both.

**Counting.** Add 1 for each letter of `s`, subtract 1 for each letter of `t`. All 26 counters end at zero exactly for anagrams.

* Time: **O(n)** — one pass over each string.
* Space: **O(1)** — 26 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0242/v2/ValidAnagram.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0242/v2/ValidAnagramTest.java` | JUnit 6 tests |
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

* [v1-sort-both-strings](../v1-sort-both-strings/README.md): Sort both strings (`O(n log n)` time, `O(n)` space)
