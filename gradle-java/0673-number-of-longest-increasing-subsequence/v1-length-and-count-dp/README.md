# 673. Number of Longest Increasing Subsequence — v1: Length and count DP

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)

## Problem

Return the number of **longest strictly increasing** subsequences of `nums`.

**Example**
```
[1,3,5,4,7] → 2   ([1,3,4,7] and [1,3,5,7])
[2,2,2,2,2] → 5   (each single element)
```

**Constraints**
* `1 <= nums.length <= 2000`

## Approach: Length and count DP

> Alongside the LIS length ending at each index, keep how many subsequences achieve it.

**Two arrays.** `len[i]` is the longest increasing subsequence ending at `i`, `cnt[i]` how many reach that length. For each `j < i` with
`nums[j] < nums[i]`: a longer chain `len[j] + 1 > len[i]` replaces the count with `cnt[j]`; an equal one adds `cnt[j]`. Finally add up the
counts of all positions whose length is the maximum.

* Time: **O(n²)**.
* Space: **O(n)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0673/v1/NumberOfLIS.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0673/v1/NumberOfLISTest.java` | JUnit 6 tests |
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
