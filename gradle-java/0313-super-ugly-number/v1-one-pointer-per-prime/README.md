# 313. Super Ugly Number — v1: One pointer per prime

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/super-ugly-number/)

## Problem

A **super ugly number** is a positive integer whose prime factors all appear in the array `primes`. Return the `n`-th super ugly number
(1 is the first). The answer fits in a 32-bit signed integer.

**Example**
```
n = 12, primes = [2,7,13,19] → 32
   (1,2,4,7,8,13,14,16,19,26,28,32)
n = 1,  primes = [2,3,5]     → 1
```

**Constraints**
* `1 <= n <= 10^5`, `1 <= primes.length <= 100`, primes are distinct and sorted

## Approach: One pointer per prime

> The three-pointer merge from Ugly Number II, with one pointer per prime.

**k-way merge.** Every super ugly number is a smaller one times some prime. Keep a pointer `idx[j]` per prime: the smallest number not
yet multiplied by `primes[j]`. The next number is the smallest candidate `ugly[idx[j]] * primes[j]`; advance every pointer that produced
it to skip duplicates. Candidates can exceed 32 bits, so use `long`.

* Time: **O(n · k)** — `k` candidates per number.
* Space: **O(n + k)** — the sequence and pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0313/v1/SuperUglyNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0313/v1/SuperUglyNumberTest.java` | JUnit 6 tests |
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
