# 264. Ugly Number II — v2: Three pointers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/ugly-number-ii/)

## Problem

Return the `n`-th ugly number (prime factors only 2, 3 and 5; the sequence starts `1, 2, 3, 4, 5, 6, 8, 9, 10, 12, …`).

**Example**
```
n = 10 → 12
n = 1  → 1
```

**Constraints**
* `1 <= n <= 1690`

## Approach: Three pointers

> Every ugly number is a smaller ugly number times 2, 3 or 5; merge those three sequences with three pointers.

**Merge three streams.** The sequence times 2, times 3 and times 5 are each sorted. Keep a pointer into the sequence for each factor. The
next ugly number is the smallest of the three candidates; advance **every** pointer that produced it, so duplicates such as `6 = 2·3 =
3·2` appear once.

* Time: **O(n)** — one step per number.
* Space: **O(n)** — the sequence.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0264/v2/UglyNumberII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0264/v2/UglyNumberIITest.java` | JUnit 6 tests |
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

* [v1-min-heap-with-a-seen-set](../v1-min-heap-with-a-seen-set/README.md): Min-heap with a seen set (`O(n log n)` time, `O(n)` space)
