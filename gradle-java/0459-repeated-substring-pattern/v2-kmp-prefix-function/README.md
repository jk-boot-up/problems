# 459. Repeated Substring Pattern — v2: KMP prefix function

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

## Approach: KMP prefix function

> The KMP failure function gives the shortest period; the string repeats iff that period divides its length.

**Shortest period.** `lps[i]` is the length of the longest proper prefix of `s[0..i]` that is also a suffix. For the whole string,
`p = n - lps[n-1]` is its shortest period. `s` is a repetition iff `lps[n-1] > 0` and `n % p == 0`.

* Time: **O(n)** — building `lps`.
* Space: **O(n)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0459/v2/RepeatedSubstringPattern.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0459/v2/RepeatedSubstringPatternTest.java` | JUnit 6 tests |
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

* [v1-doubled-string-trick](../v1-doubled-string-trick/README.md): Doubled-string trick (`O(n²)` time, `O(n)` space)
