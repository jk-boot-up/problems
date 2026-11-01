# 1405. Longest Happy String — v1: Greedy by remaining count

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/longest-happy-string/)

## Problem

A string is **happy** if it uses only `'a'`, `'b'`, `'c'`, never contains `"aaa"`, `"bbb"` or `"ccc"`, and uses at most `a`, `b`, `c`
copies of each letter. Return any longest happy string (`""` if none).

**Example**
```
a = 1, b = 1, c = 7 → "ccaccbcc"  (length 8)
a = 7, b = 1, c = 0 → "aabaa"     (length 5)
```

**Constraints**
* `0 <= a, b, c <= 100`, `a + b + c > 0`

## Approach: Greedy by remaining count

> Always append the letter with the most copies left, unless that would make three in a row; then use the next one.

**Spend the biggest pile.** Repeatedly try the letters from most to fewest remaining copies. Append the first one that would not create
three equal letters in a row. Stop when nothing can be appended. Using the largest pile whenever allowed keeps the others available as
separators for as long as possible.

* Time: **O(a + b + c)** — one letter per round (sorting three items is constant).
* Space: **O(1)** — besides the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1405/v1/LongestHappyString.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1405/v1/LongestHappyStringTest.java` | JUnit 6 tests |
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
