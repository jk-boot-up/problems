# 151. Reverse Words in a String — v2: Manual right-to-left scan

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

## Approach: Manual right-to-left scan

> Scan from the right, cut out each word, and append it; spaces collapse naturally.

**Right-to-left scan.** Walk `i` from the end. Skip spaces; mark `end`; move `i` left while it points at a non-space;
the word is `s[i+1 .. end]`. Append it to a `StringBuilder`, with a space before every word but the first.

* Time: **O(n)** — every character is visited once and copied once.
* Space: **O(n)** — the output builder.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0151/v2/ReverseWords.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0151/v2/ReverseWordsTest.java` | JUnit 6 tests |
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

* [v1-split-reverse-join](../v1-split-reverse-join/README.md): Split, reverse, join (`O(n)` time, `O(n)` space)
