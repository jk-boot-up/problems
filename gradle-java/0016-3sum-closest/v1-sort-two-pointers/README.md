# 16. 3Sum Closest — v1: Sort + two pointers

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/3sum-closest/)

## Problem

Find three numbers in `nums` whose sum is closest to `target` and return that sum. Exactly one answer exists.

**Example**
```
nums = [-1,2,1,-4], target = 1 → 2   (-1 + 2 + 1)
nums = [0,0,0], target = 1     → 0
```

**Constraints**
* `3 <= nums.length <= 500`

## Approach: Sort + two pointers

> Sort, fix one number, and move two pointers toward the target sum, remembering the closest sum seen.

**Two pointers per fixed element.** Sort. For each `i`, move `l` and `r` inward: if the sum is below the target, `l++`; above, `r--`;
equal, return immediately. Track the sum with the smallest distance.

* Time: **O(n²)** — n fixed values × a linear scan.
* Space: **O(log n)** — sorting.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0016/v1/ThreeSumClosest.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0016/v1/ThreeSumClosestTest.java` | JUnit 6 tests |
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
