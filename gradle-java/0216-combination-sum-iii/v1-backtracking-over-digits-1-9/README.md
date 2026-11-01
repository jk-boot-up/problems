# 216. Combination Sum III — v1: Backtracking over digits 1–9

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/combination-sum-iii/)

## Problem

Find all combinations of `k` **distinct** digits from `1` to `9` that add up to `n`. Return each combination once, in any order.

**Example**
```
k = 3, n = 7 → [[1,2,4]]
k = 3, n = 9 → [[1,2,6],[1,3,5],[2,3,4]]
k = 4, n = 1 → []
```

**Constraints**
* `2 <= k <= 9`, `1 <= n <= 60`

## Approach: Backtracking over digits 1–9

> Pick digits in increasing order and stop a branch as soon as the sum or the count overshoots.

**Increasing choices.** Choosing digits in increasing order makes each combination appear once. From `start`, try each digit `d` no larger
than the remaining sum, recurse with `d + 1`, then undo. Record the path when it has `k` digits and the remainder is 0.

* Time: **O(C(9, k) · k)** — at most `C(9, k)` complete paths, each copied once.
* Space: **O(k)** — the recursion depth and path.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0216/v1/CombinationSumIII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0216/v1/CombinationSumIIITest.java` | JUnit 6 tests |
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
