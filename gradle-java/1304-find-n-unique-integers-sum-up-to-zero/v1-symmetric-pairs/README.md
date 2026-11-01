# 1304. Find N Unique Integers Sum up to Zero — v1: Symmetric pairs

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/)

## Problem

Return any array of `n` **distinct** integers that add up to 0.

**Example**
```
n = 5 → [-2,-1,0,1,2]   (any valid answer is accepted)
n = 1 → [0]
```

**Constraints**
* `1 <= n <= 1000`

## Approach: Symmetric pairs

> Pair each k with −k; add a 0 when n is odd.

**Mirror pairs.** Put `k` and `-k` for `k = 1..n/2`; each pair cancels. If `n` is odd, the remaining slot holds `0`.

* Time: **O(n)**.
* Space: **O(1)** — besides the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1304/v1/SumZero.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1304/v1/SumZeroTest.java` | JUnit 6 tests |
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
