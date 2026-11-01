# 485. Max Consecutive Ones — v1: Running count

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/max-consecutive-ones/)

## Problem

Return the maximum number of consecutive `1`s in a binary array.

**Example**
```
[1,1,0,1,1,1] → 3,   [1,0,1,1,0,1] → 2
```

**Constraints**
* `1 <= n <= 10^5`

## Approach: Running count

> Count the current run of 1s, reset on 0, and remember the longest run.

**One pass.** `run = x == 1 ? run + 1 : 0`; track the maximum.

* Time: **O(n)** — one pass.
* Space: **O(1)** — two counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0485/v1/MaxConsecutiveOnes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0485/v1/MaxConsecutiveOnesTest.java` | JUnit 6 tests |
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
