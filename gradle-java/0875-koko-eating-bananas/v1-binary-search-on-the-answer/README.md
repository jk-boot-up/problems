# 875. Koko Eating Bananas — v1: Binary search on the answer

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/koko-eating-bananas/)

## Problem

Koko eats bananas from `piles` at `k` bananas per hour, finishing one pile before moving on (an hour with fewer than `k` left in a pile is
still a full hour). Return the minimum `k` that lets her finish within `h` hours.

**Example**
```
piles = [3,6,7,11], h = 8 → 4,   piles = [30,11,23,4,20], h = 5 → 30
```

**Constraints**
* `piles.length <= h <= 10^9`; `1 <= piles[i] <= 10^9`

## Approach: Binary search on the answer

> Binary-search the eating speed: a faster speed never needs more hours.

**Monotone predicate.** Hours needed at speed `k` is `Σ ceil(p / k)`, which only decreases as `k` grows. Binary-search the smallest `k`
in `[1, max(piles)]` with `hours <= h` (sum in a `long`).

* Time: **O(n log M)** — M is the largest pile.
* Space: **O(1)** — a few variables.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0875/v1/KokoEatingBananas.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0875/v1/KokoEatingBananasTest.java` | JUnit 6 tests |
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
