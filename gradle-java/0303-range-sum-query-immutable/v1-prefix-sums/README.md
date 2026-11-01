# 303. Range Sum Query - Immutable — v1: Prefix sums

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Prefix Sum &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/range-sum-query-immutable/)

## Problem

Implement `NumArray`:

* `NumArray(int[] nums)`
* `int sumRange(int left, int right)` — the sum of `nums[left..right]` inclusive.

**Example**
```
nums = [-2,0,3,-5,2,-1]
sumRange(0,2) → 1, sumRange(2,5) → -1, sumRange(0,5) → -3
```

**Constraints**
* `1 <= nums.length <= 10^4`, up to `10^4` queries

## Approach: Prefix sums

> Precompute prefix sums once; any range sum is the difference of two prefixes.

**Prefix sums.** Store `prefix[i] = nums[0] + … + nums[i-1]` with `prefix[0] = 0`. Then
`sumRange(l, r) = prefix[r + 1] - prefix[l]`.

* Time: **O(1)** — per query, after O(n) setup.
* Space: **O(n)** — the prefix array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0303/v1/NumArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0303/v1/NumArrayTest.java` | JUnit 6 tests |
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
