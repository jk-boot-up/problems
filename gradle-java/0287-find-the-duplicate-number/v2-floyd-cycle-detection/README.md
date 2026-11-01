# 287. Find the Duplicate Number — v2: Floyd cycle detection

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/)

## Problem

`nums` has `n + 1` integers, each in `[1, n]`. Exactly one value is repeated (possibly many times). Return it without modifying the
array and using O(1) extra space.

**Example**
```
[1,3,4,2,2] → 2,   [3,1,3,4,2] → 3,   [3,3,3,3,3] → 3
```

**Constraints**
* `1 <= n <= 10^5`

## Approach: Floyd cycle detection

> Treat i → nums[i] as a linked list; the duplicate is where the cycle begins (Floyd).

**Cycle entrance.** Follow `x → nums[x]` from 0. Two indices point to the duplicate value, so the path forms a cycle whose entrance
is the duplicate. Phase 1: slow (1 step) and fast (2 steps) meet inside the cycle. Phase 2: restart one pointer at 0 and move both one
step at a time; they meet at the entrance.

* Time: **O(n)** — both phases are linear.
* Space: **O(1)** — two indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0287/v2/FindDuplicate.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0287/v2/FindDuplicateTest.java` | JUnit 6 tests |
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

* [v1-seen-set](../v1-seen-set/README.md): Seen set (`O(n)` time, `O(n)` space)
