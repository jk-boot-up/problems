# 88. Merge Sorted Array — v2: Three pointers from the back

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/merge-sorted-array/)

## Problem

You get two integer arrays `nums1` and `nums2`, both sorted in non-decreasing order, plus two counts `m` and `n`.
Only the first `m` values of `nums1` are real; its last `n` slots hold `0` as placeholders. `nums2` holds exactly `n` values.

Merge `nums2` into `nums1` **in place** so that `nums1` becomes one sorted array of length `m + n`. The method returns nothing.

**Example 1**
```
Input:  nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: nums1 = [1,2,2,3,5,6]
```

**Example 2**
```
Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
Output: nums1 = [1]
```

**Constraints**
* `nums1.length == m + n`, `nums2.length == n`
* `0 <= m, n <= 200`, `1 <= m + n <= 200`
* `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Approach: Three pointers from the back

> Fill nums1 from the back with the larger of the two current tails, so nothing unread is overwritten.

**Three pointers, writing from the back.** `i` points at the last real value of `nums1`, `j` at the last value of `nums2`,
and `k` at the last slot of `nums1`. At every step copy the larger of `nums1[i]` and `nums2[j]` into `nums1[k]`, then move
the pointer you copied from, and `k`, one step left. Writing from the back means we only ever overwrite slots we have already read.
When `nums2` runs out, the rest of `nums1` is already in place.

* Time: **O(m + n)** — every slot of nums1 is written exactly once.
* Space: **O(1)** — only three index variables.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0088/v2/MergeSortedArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0088/v2/MergeSortedArrayTest.java` | JUnit 6 tests |
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

* [v1-copy-and-sort](../v1-copy-and-sort/README.md): Copy and sort (`O((m + n) log(m + n))` time, `O(log(m + n))` space)
