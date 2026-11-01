# 410. Split Array Largest Sum — v2: Binary search on the cap

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

## Approach: Binary search on the cap

> Binary search on the answer: can the array be cut into at most k pieces whose sums stay below a cap?

**Feasibility is monotone.** For a cap `c`, greedily extend the current piece until the next number would exceed `c`, then start a new
piece. If that needs at most `k` pieces, any larger cap works too. Binary search `c` between `max(nums)` (each number must fit) and
`sum(nums)` (one piece). Fewer than `k` pieces is fine, since pieces can always be split further.

* Time: **O(n log S)** — `S` is the sum; each check is linear.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0410/v2/SplitArrayLargestSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0410/v2/SplitArrayLargestSumTest.java` | JUnit 6 tests |
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

* [v1-dp-over-prefixes-and-pieces](../v1-dp-over-prefixes-and-pieces/README.md): DP over prefixes and pieces (`O(k · n²)` time, `O(k · n)` space)
