# 319. Bulb Switcher — v1: Count perfect squares

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/bulb-switcher/)

## Problem

There are `n` bulbs, all off. In round `i` (for `i = 1..n`) you toggle every `i`-th bulb. Return how many bulbs are on after `n` rounds.

**Example**
```
n = 3 → 1
n = 0 → 0
n = 1 → 1
```

**Constraints**
* `0 <= n <= 10^9`

## Approach: Count perfect squares

> Bulb i is toggled once per divisor; only perfect squares have an odd number of divisors.

**Divisors pair up.** Bulb `k` is toggled in every round `d` that divides `k`. Divisors come in pairs `d` and `k / d`, except when
`d = √k`. So bulb `k` ends on exactly when `k` is a perfect square, and there are `⌊√n⌋` of those up to `n`.

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0319/v1/BulbSwitcher.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0319/v1/BulbSwitcherTest.java` | JUnit 6 tests |
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
