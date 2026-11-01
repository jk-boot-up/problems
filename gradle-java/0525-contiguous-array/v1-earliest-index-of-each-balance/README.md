# 525. Contiguous Array — v1: Earliest index of each balance

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contiguous-array/)

## Problem

Given a binary array, return the length of the longest contiguous subarray with an equal number of 0s and 1s.

**Example**
```
[0,1]                 → 2
[0,1,0]               → 2
[0,1,1,1,1,1,0,0,0]   → 6
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Approach: Earliest index of each balance

> Count 0 as −1; equal running balances mark a stretch with as many 0s as 1s.

**Balance.** Add +1 for a 1 and -1 for a 0. A subarray is balanced exactly when the running balance is the same at both ends. The balance
stays within `[-n, n]`, so a plain array (offset by `n`) stores the earliest index of each balance; no hash map is needed.

* Time: **O(n)**.
* Space: **O(n)** — the `2n + 1` slots.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0525/v1/ContiguousArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0525/v1/ContiguousArrayTest.java` | JUnit 6 tests |
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
