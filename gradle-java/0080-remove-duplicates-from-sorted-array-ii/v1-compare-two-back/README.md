# 80. Remove Duplicates from Sorted Array II — v1: Compare two back

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## Problem

`nums` is sorted in non-decreasing order. Remove extra duplicates **in place** so that every distinct value appears **at most twice**,
keeping the relative order. Return `k`, the length of the result; the first `k` slots of `nums` must hold it. Use O(1) extra memory.

**Example 1**
```
Input:  nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
```

**Example 2**
```
Input:  nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`
* `-10^4 <= nums[i] <= 10^4`, sorted non-decreasing

## Approach: Compare two back

> Keep a value only if it differs from the value two slots back in the kept prefix.

**Compare with two back.** Keep a write index `k`. A value `x` may be written if `k < 2` or `x != nums[k - 2]`. If it equals
`nums[k-2]`, then because the array is sorted, `nums[k-2]` and `nums[k-1]` are both `x` already, so writing it would make a third copy.

* Time: **O(n)** — a single pass.
* Space: **O(1)** — in-place overwrite with one write index.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0080/v1/RemoveDuplicatesII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0080/v1/RemoveDuplicatesIITest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
