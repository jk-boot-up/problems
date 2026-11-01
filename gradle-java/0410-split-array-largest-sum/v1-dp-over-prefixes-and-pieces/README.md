# 410. Split Array Largest Sum — v1: DP over prefixes and pieces

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/split-array-largest-sum/)

## Problem

Split `nums` into `k` non-empty contiguous subarrays so that the **largest** subarray sum is as small as possible. Return that sum.

**Example**
```
nums = [7,2,5,10,8], k = 2 → 18   ([7,2,5] and [10,8])
nums = [1,2,3,4,5],  k = 2 → 9
nums = [1,4,4],      k = 3 → 4
```

**Constraints**
* `1 <= nums.length <= 1000`, `0 <= nums[i] <= 10^6`, `1 <= k <= min(50, nums.length)`

## Approach: DP over prefixes and pieces

> best[j][i] = the best largest sum for the first i numbers in j pieces, trying every position for the last cut.

**DP.** With prefix sums, `best[j][i] = min over p < i of max(best[j-1][p], sum(p..i-1))`. The answer is `best[k][n]`.

* Time: **O(k · n²)** — `k · n` states, each trying `n` cut positions.
* Space: **O(k · n)** — the table.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0410/v1/SplitArrayLargestSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0410/v1/SplitArrayLargestSumTest.java` | JUnit 6 tests |
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

* [v2-binary-search-on-the-cap](../v2-binary-search-on-the-cap/README.md): Binary search on the cap (`O(n log S)` time, `O(1)` space)
