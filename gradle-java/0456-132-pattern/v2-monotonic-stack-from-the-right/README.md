# 456. 132 Pattern — v2: Monotonic stack from the right

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

## Approach: Monotonic stack from the right

> Scan from the right with a decreasing stack; values popped become the best '2', and any smaller element is the '1'.

**Right to left.** Keep a stack of candidates for the "3", decreasing from bottom to top, and `third`, the largest value that has been
popped (a valid "2": something bigger sits to its left). When a new value is bigger than the top, pop: each popped value has a bigger
"3" left of it, so it can serve as "2". If a value is smaller than `third`, it is the "1".

* Time: **O(n)** — each value is pushed and popped once.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0456/v2/Pattern132.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0456/v2/Pattern132Test.java` | JUnit 6 tests |
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

* [v1-prefix-minimum-check-every-pair](../v1-prefix-minimum-check-every-pair/README.md): Prefix minimum, check every pair (`O(n²)` time, `O(1)` space)
