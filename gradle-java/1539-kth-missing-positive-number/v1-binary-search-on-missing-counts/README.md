# 1539. Kth Missing Positive Number — v1: Binary search on missing counts

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-missing-positive-number/)

## Problem

Given a strictly increasing array of positive integers and `k`, return the `k`-th positive integer missing from the array.

**Example**
```
arr = [2,3,4,7,11], k = 5 → 9    (missing: 1,5,6,8,9,…)
arr = [1,2,3,4],    k = 2 → 6
```

**Constraints**
* `1 <= arr.length <= 1000`, `1 <= arr[i], k <= 1000`

## Approach: Binary search on missing counts

> arr[i] − (i + 1) counts the positives missing before arr[i]; binary search where that count reaches k.

**Missing counter.** Before `arr[i]` there are `arr[i] - (i + 1)` missing positives, and this count never decreases. Binary search for the
first index `lo` whose count is at least `k`. Exactly `lo` array values are below the answer, so the answer is `lo + k`.

* Time: **O(log n)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1539/v1/KthMissingPositive.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1539/v1/KthMissingPositiveTest.java` | JUnit 6 tests |
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
