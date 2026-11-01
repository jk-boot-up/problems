# 318. Maximum Product of Word Lengths — v1: Letter bitmasks

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-product-of-word-lengths/)

## Problem

Return the maximum value of `length(a) * length(b)` over two words of `words` that share **no** letters. Return 0 if no such pair exists.

**Example**
```
["abcw","baz","foo","bar","xtfn","abcdef"] → 16   ("abcw", "xtfn")
["a","ab","abc","d","cd","bcd","abcd"]     → 4    ("ab", "cd")
["a","aa","aaa","aaaa"]                    → 0
```

**Constraints**
* `2 <= words.length <= 1000`, lower-case words of length at most 1000

## Approach: Letter bitmasks

> A 26-bit mask per word turns 'no common letters' into a single AND.

**Masks.** Bit `c` of `mask[i]` is set when word `i` contains letter `c`. Two words share no letter exactly when `mask[i] & mask[j] == 0`.
Compare every pair in O(1).

* Time: **O(L + n²)** — `L` letters to build the masks, then all pairs.
* Space: **O(n)** — one mask per word.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0318/v1/MaxProductWordLengths.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0318/v1/MaxProductWordLengthsTest.java` | JUnit 6 tests |
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
