# 15. 3Sum — v2: Sort + two pointers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/3sum/)

## Problem

Return all **unique** triplets `[a, b, c]` from `nums` (at different indices) with `a + b + c == 0`. The answer must not
contain duplicate triplets; order does not matter.

**Example 1**
```
Input:  nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2**
```
Input:  nums = [0,1,1]
Output: []
```

**Example 3**
```
Input:  nums = [0,0,0]
Output: [[0,0,0]]
```

**Constraints**
* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

## Approach: Sort + two pointers

> Sort, fix the first number, then find pairs summing to its negative with two pointers, skipping duplicates.

**Sort + two pointers.** Sort the array. For each `i` (skipping a value equal to the previous one), search `i+1..n-1` with `l`
and `r` for pairs summing to `-nums[i]`. On a hit, record it and skip equal neighbours on both sides. Stop once
`nums[i] > 0`, because then all three numbers are positive.

* Time: **O(n²)** — n choices of i, each with a linear two-pointer scan (the sort is O(n log n)).
* Space: **O(1)** — apart from sorting and the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0015/v2/ThreeSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0015/v2/ThreeSumTest.java` | JUnit 6 tests |
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

* [v1-hash-set-per-fixed-number](../v1-hash-set-per-fixed-number/README.md): Hash set per fixed number (`O(n²)` time, `O(n)` space)
