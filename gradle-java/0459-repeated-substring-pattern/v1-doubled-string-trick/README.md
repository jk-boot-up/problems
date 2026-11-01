# 459. Repeated Substring Pattern — v1: Doubled-string trick

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/repeated-substring-pattern/)

## Problem

Return `true` if `s` can be built by repeating one of its substrings two or more times.

**Example**
```
"abab"         → true   ("ab" × 2)
"aba"          → false
"abcabcabcabc" → true
```

**Constraints**
* `1 <= s.length <= 10^4`

## Approach: Doubled-string trick

> s is a repetition iff it appears inside (s + s) with the first and last characters removed.

**Rotation.** If `s` is built from a repeated block, rotating it by the block length gives `s` back, so `s` occurs inside `s + s` at a
position other than `0` and `n`. Cutting off the first and last characters removes exactly those two trivial matches.

* Time: **O(n²)** — `String.contains` worst case (O(n) with a linear matcher).
* Space: **O(n)** — the doubled string.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0459/v1/RepeatedSubstringPattern.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0459/v1/RepeatedSubstringPatternTest.java` | JUnit 6 tests |
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

* [v2-kmp-prefix-function](../v2-kmp-prefix-function/README.md): KMP prefix function (`O(n)` time, `O(n)` space)
