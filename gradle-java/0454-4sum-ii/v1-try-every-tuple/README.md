# 454. 4Sum II — v1: Try every tuple

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/4sum-ii/)

## Problem

Given four arrays of length `n`, count tuples `(i, j, k, l)` with `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0`.

**Example**
```
nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2] → 2
nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0] → 1
```

**Constraints**
* `1 <= n <= 200`, `-2^28 <= values <= 2^28`

## Approach: Try every tuple

> Four nested loops over all n⁴ tuples.

**Brute force.** Check every `(i, j, k, l)`.

* Time: **O(n⁴)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0454/v1/FourSumII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0454/v1/FourSumIITest.java` | JUnit 6 tests |
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

* [v2-pair-sums-in-a-hash-map](../v2-pair-sums-in-a-hash-map/README.md): Pair sums in a hash map (`O(n²)` time, `O(n²)` space)
