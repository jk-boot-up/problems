# 299. Bulls and Cows — v1: One pass with a signed tally

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/bulls-and-cows/)

## Problem

Given a `secret` and a `guess` of the same length (digits only), return the hint `"xAyB"`: `x` **bulls** (right digit, right position)
and `y` **cows** (digits in the guess that are in the secret but in the wrong position, each secret digit used at most once).

**Example**
```
secret = "1807", guess = "7810" → "1A3B"
secret = "1123", guess = "0111" → "1A1B"
```

**Constraints**
* `1 <= length <= 1000`

## Approach: One pass with a signed tally

> Count exact matches; for the rest, a signed digit tally tells you when a digit has a partner on the other side.

**Signed counts.** For each position that is not a bull, add 1 for the secret digit and subtract 1 for the guess digit. If the secret
digit's tally was negative, an earlier guess digit was waiting for it: a cow. If the guess digit's tally was positive, an earlier secret
digit was waiting: a cow.

* Time: **O(n)** — one pass.
* Space: **O(1)** — ten counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0299/v1/BullsAndCows.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0299/v1/BullsAndCowsTest.java` | JUnit 6 tests |
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
