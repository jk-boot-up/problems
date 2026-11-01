# 228. Summary Ranges — v1: Single scan

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Intervals &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/summary-ranges/)

## Problem

`nums` is sorted and has no duplicates. Return the smallest sorted list of ranges that covers every number exactly. A range
`[a,b]` is written `"a->b"` if `a != b`, else `"a"`.

**Example 1**
```
Input:  nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
```

**Example 2**
```
Input:  nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
```

**Constraints**
* `0 <= nums.length <= 20`; values fit in 32-bit integers; sorted, unique.

## Approach: Single scan

> Walk the sorted unique values, extending a range while the next value is exactly one more.

**Grow each range.** Mark a range start `i`; advance `j` while `nums[j+1] == nums[j] + 1`. Emit the range and continue from `j + 1`.

* Time: **O(n)** — each value is visited once.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0228/v1/SummaryRanges.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0228/v1/SummaryRangesTest.java` | JUnit 6 tests |
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
