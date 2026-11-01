# 1283. Find the Smallest Divisor Given a Threshold — v1: Binary search on the divisor

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

## Problem

Choose a positive integer divisor, divide every element of `nums` by it rounding **up**, and add the results. Return the smallest divisor
for which this sum is at most `threshold`.

**Example**
```
nums = [1,2,5,9], threshold = 6 → 5   (1 + 1 + 1 + 2 = 5)
nums = [44,22,33,11,1], threshold = 5 → 44
```

**Constraints**
* `1 <= nums.length <= 5 * 10^4 <= threshold <= 10^6`, `1 <= nums[i] <= 10^6`

## Approach: Binary search on the divisor

> The rounded-up quotient sum only shrinks as the divisor grows, so binary search for the first divisor that fits.

**Monotone check.** A larger divisor never increases any `ceil(x / d)`, so the sum is non-increasing in `d`. Binary search `d` in
`1..max(nums)` (at `max`, every term is 1 and the sum is `n <= threshold`). `ceil(x / d)` is `(x + d - 1) / d`.

* Time: **O(n log M)** — `M = max(nums)`.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1283/v1/SmallestDivisor.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1283/v1/SmallestDivisorTest.java` | JUnit 6 tests |
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
