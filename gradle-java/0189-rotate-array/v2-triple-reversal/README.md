# 189. Rotate Array — v2: Triple reversal

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rotate-array/)

## Problem

Rotate the integer array `nums` to the right by `k` steps, in place. `k` is non-negative and may be larger than the array length.

**Example 1**
```
Input:  nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

**Example 2**
```
Input:  nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

**Constraints**
* `1 <= nums.length <= 10^5`
* `-2^31 <= nums[i] <= 2^31 - 1`
* `0 <= k <= 10^5`

**Follow-up:** can you do it in place with O(1) extra space?

## Approach: Triple reversal

> Rotate right by k with three reversals: the whole array, then the first k, then the rest.

**Triple reversal.** Let `k = k % n`. Reverse the whole array: the last `k` values move to the front, but in reverse order.
Then reverse the first `k` values and the remaining `n - k` values to restore their order.

* Time: **O(n)** — every element is swapped at most twice.
* Space: **O(1)** — swaps happen in place.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0189/v2/RotateArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0189/v2/RotateArrayTest.java` | JUnit 6 tests |
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

* [v1-extra-array](../v1-extra-array/README.md): Extra array (`O(n)` time, `O(n)` space)
