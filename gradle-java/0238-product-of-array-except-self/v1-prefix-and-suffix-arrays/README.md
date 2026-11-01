# 238. Product of Array Except Self — v1: Prefix and suffix arrays

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

## Problem

Given an integer array `nums`, return an array `answer` where `answer[i]` equals the product of every element of `nums`
**except** `nums[i]`. Do it in O(n) time **without using division**. Every prefix/suffix product fits in a 32-bit integer.

**Example 1**
```
Input:  nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2**
```
Input:  nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints**
* `2 <= nums.length <= 10^5`
* `-30 <= nums[i] <= 30`

**Follow-up:** O(1) extra space (the output array does not count).

## Approach: Prefix and suffix arrays

> Precompute products to the left and to the right of every index, then multiply them.

**Two helper arrays.** `left[i]` = product of `nums[0..i-1]`, `right[i]` = product of `nums[i+1..n-1]`;
`answer[i] = left[i] * right[i]`.

* Time: **O(n)** — three linear passes.
* Space: **O(n)** — two extra arrays besides the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0238/v1/ProductExceptSelf.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0238/v1/ProductExceptSelfTest.java` | JUnit 6 tests |
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

* [v2-output-array-running-suffix](../v2-output-array-running-suffix/README.md): Output array + running suffix (`O(n)` time, `O(1)` space)
