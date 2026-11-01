# 238. Product of Array Except Self — v2: Output array + running suffix

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

## Approach: Output array + running suffix

> answer[i] = (product of everything left of i) × (product of everything right of i), built in two passes.

**Prefix and suffix products.** First pass, left to right: `answer[i]` = product of all values before `i`.
Second pass, right to left: keep a running `suffix` product and multiply it into `answer[i]`.

* Time: **O(n)** — two linear passes.
* Space: **O(1)** — besides the output, only the running suffix product.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0238/v2/ProductExceptSelf.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0238/v2/ProductExceptSelfTest.java` | JUnit 6 tests |
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
  engine (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-prefix-and-suffix-arrays](../v1-prefix-and-suffix-arrays/README.md): Prefix and suffix arrays (`O(n)` time, `O(n)` space)
