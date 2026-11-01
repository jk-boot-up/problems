# 456. 132 Pattern — v1: Prefix minimum, check every pair

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Monotonic Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/132-pattern/)

## Problem

Return `true` if there are indices `i < j < k` with `nums[i] < nums[k] < nums[j]` (a "132" shape).

**Example**
```
[1,2,3,4]  → false
[3,1,4,2]  → true    (1, 4, 2)
[-1,3,2,0] → true
```

**Constraints**
* `1 <= nums.length <= 2 * 10^5`

## Approach: Prefix minimum, check every pair

> For each j, the best '1' is the minimum to its left; look for a k with that minimum < nums[k] < nums[j].

**Fix the middle.** Track the smallest value before `j`. For each later `k`, check `min < nums[k] < nums[j]`.

* Time: **O(n²)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0456/v1/Pattern132.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0456/v1/Pattern132Test.java` | JUnit 6 tests |
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

* [v2-monotonic-stack-from-the-right](../v2-monotonic-stack-from-the-right/README.md): Monotonic stack from the right (`O(n)` time, `O(n)` space)
