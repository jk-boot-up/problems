# 135. Candy — v1: Two passes

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/candy/)

## Problem

`n` children stand in a line; `ratings[i]` is child `i`'s rating. Give out candies so that:
* every child gets at least one candy, and
* a child with a higher rating than a neighbour gets more candies than that neighbour.

Return the minimum total number of candies.

**Example 1**
```
Input:  ratings = [1,0,2]
Output: 5   (2, 1, 2)
```

**Example 2**
```
Input:  ratings = [1,2,2]
Output: 4   (1, 2, 1)
```

**Constraints**
* `1 <= n <= 2 * 10^4`
* `0 <= ratings[i] <= 2 * 10^4`

## Approach: Two passes

> Satisfy left neighbours in one pass and right neighbours in a second pass, taking the max at each child.

**Two passes.** Start everyone at 1. Left to right: if `ratings[i] > ratings[i-1]`, set `candy[i] = candy[i-1] + 1`.
Right to left: if `ratings[i] > ratings[i+1]`, set `candy[i] = max(candy[i], candy[i+1] + 1)`. Both rules now hold with the
fewest candies.

* Time: **O(n)** — two passes.
* Space: **O(n)** — the candy array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0135/v1/Candy.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0135/v1/CandyTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
