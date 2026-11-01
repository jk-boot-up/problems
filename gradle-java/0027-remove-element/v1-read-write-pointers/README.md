# 27. Remove Element — v1: Read-write pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-element/)

## Problem

Given an integer array `nums` and an integer `val`, remove every occurrence of `val` **in place** and return `k`, the number
of elements that are not equal to `val`. The first `k` slots of `nums` must hold those elements (in any order); what remains after
index `k - 1` does not matter.

**Example 1**
```
Input:  nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

**Example 2**
```
Input:  nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,3,0,4,_,_,_]
```

**Constraints**
* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 50`, `0 <= val <= 100`

## Approach: Read-write pointers

> A write pointer keeps every value that is not val; the reader skips the ones that are.

**Read/write pointers.** Scan the array with a reader `i`. Whenever `nums[i] != val`, copy it to `nums[k]` and advance `k`.
At the end, `k` is the number of kept values and they sit at the front.

* Time: **O(n)** — one pass over the array.
* Space: **O(1)** — the array is rewritten in place.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0027/v1/RemoveElement.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0027/v1/RemoveElementTest.java` | JUnit 6 tests |
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
