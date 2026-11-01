# 1512. Number of Good Pairs — v1: Running counts

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-good-pairs/)

## Problem

A pair `(i, j)` is good if `nums[i] == nums[j]` and `i < j`. Return the number of good pairs.

**Example**
```
[1,2,3,1,1,3] → 4,   [1,1,1,1] → 6,   [1,2,3] → 0
```

**Constraints**
* `1 <= nums.length <= 100`; `1 <= nums[i] <= 100`

## Approach: Running counts

> Each new copy of a value pairs with every earlier copy of it.

**Count as you go.** When a value appears for the k-th time, it forms `k - 1` new pairs; add the current count before incrementing it.

* Time: **O(n)** — one pass.
* Space: **O(1)** — 101 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1512/v1/NumberOfGoodPairs.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1512/v1/NumberOfGoodPairsTest.java` | JUnit 6 tests |
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
