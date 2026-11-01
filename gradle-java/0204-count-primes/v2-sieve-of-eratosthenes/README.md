# 204. Count Primes — v2: Sieve of Eratosthenes

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/count-primes/)

## Problem

Return the number of prime numbers **strictly less than** `n`.

**Example**
```
10 → 4    (2, 3, 5, 7)
0  → 0
1  → 0
```

**Constraints**
* `0 <= n <= 5 * 10^6`

## Approach: Sieve of Eratosthenes

> Cross out multiples of each prime, starting at its square; whatever survives is prime.

**Sieve.** Walk `i` upward. If `i` is not crossed out, it is prime: count it and cross out `i·i, i·i + i, …` (smaller multiples were
crossed out by smaller primes already). Use `long` for `i·i` so large `i` does not overflow.

* Time: **O(n log log n)** — the classic sieve bound.
* Space: **O(n)** — one flag per number.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0204/v2/CountPrimes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0204/v2/CountPrimesTest.java` | JUnit 6 tests |
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

* [v1-trial-division](../v1-trial-division/README.md): Trial division (`O(n√n)` time, `O(1)` space)
