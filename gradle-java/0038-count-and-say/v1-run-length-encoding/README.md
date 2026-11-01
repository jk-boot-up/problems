# 38. Count and Say — v1: Run-length encoding

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Strings &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-and-say/)

## Problem

`countAndSay(1) = "1"`; `countAndSay(n)` describes `countAndSay(n-1)` by saying, for each run of equal digits, the run length followed by the
digit. Return the `n`-th term.

**Example**
```
1 → "1",   2 → "11",   3 → "21",   4 → "1211",   5 → "111221"
```

**Constraints**
* `1 <= n <= 30`

## Approach: Run-length encoding

> Each term reads the previous one aloud: run-length encode it as (count, digit) pairs.

**Iterate.** Starting from `"1"`, build each next term by scanning runs and appending `count` then `digit`.

* Time: **O(L)** — L is the total length of all terms produced (it grows by about 30% per step).
* Space: **O(L)** — the current term.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0038/v1/CountAndSay.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0038/v1/CountAndSayTest.java` | JUnit 6 tests |
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
