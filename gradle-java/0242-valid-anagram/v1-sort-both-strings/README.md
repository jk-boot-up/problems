# 242. Valid Anagram — v1: Sort both strings

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

## Approach: Sort both strings

> Anagrams become identical strings once their letters are sorted.

**Sort and compare.** Sort the characters of both strings and compare the arrays.

* Time: **O(n log n)** — sorting.
* Space: **O(n)** — the character arrays.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0242/v1/ValidAnagram.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0242/v1/ValidAnagramTest.java` | JUnit 6 tests |
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

* [v2-letter-counts](../v2-letter-counts/README.md): Letter counts (`O(n)` time, `O(1)` space)
