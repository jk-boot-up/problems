# 151. Reverse Words in a String — v1: Split, reverse, join

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/)

## Problem

Given a string `s`, reverse the order of its **words**. A word is a run of non-space characters. The result must have exactly
one space between words and no leading or trailing spaces, even if `s` has extra spaces.

**Example 1**
```
Input:  s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2**
```
Input:  s = "  hello world  "
Output: "world hello"
```

**Example 3**
```
Input:  s = "a good   example"
Output: "example good a"
```

**Constraints**
* `1 <= s.length <= 10^4`; letters, digits and spaces; at least one word.

## Approach: Split, reverse, join

> Let the library split on runs of spaces, reverse the list, and join with single spaces.

**Library calls.** `s.trim().split("\\s+")` gives the words; reverse the list; `String.join(" ", words)`.
Short and clear, though it allocates an intermediate array.

* Time: **O(n)** — splitting, reversing and joining are linear.
* Space: **O(n)** — the array of words.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0151/v1/ReverseWords.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0151/v1/ReverseWordsTest.java` | JUnit 6 tests |
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

* [v2-manual-right-to-left-scan](../v2-manual-right-to-left-scan/README.md): Manual right-to-left scan (`O(n)` time, `O(n)` space)
