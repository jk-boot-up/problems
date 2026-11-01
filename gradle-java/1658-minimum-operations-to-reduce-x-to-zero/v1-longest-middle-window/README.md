# 1658. Minimum Operations to Reduce X to Zero — v1: Longest middle window

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

## Problem

In one operation, remove the leftmost or rightmost element of `nums` and subtract it from `x`. Return the minimum number of operations to
make `x` exactly 0, or `-1`.

**Example**
```
nums = [1,1,4,2,3],    x = 5  → 2   (remove 3 and 2)
nums = [5,6,7,8,9],    x = 4  → -1
nums = [3,2,20,1,1,3], x = 10 → 5
```

**Constraints**
* `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^4`, `1 <= x <= 10^9`

## Approach: Longest middle window

> Removing from both ends leaves a middle block summing to total − x; find the longest such block.

**Flip the view.** Whatever is removed is a prefix plus a suffix; what is left is a contiguous block with sum `total - x`. Fewest removals
means the **longest** such block. All values are positive, so a sliding window finds it: grow the right end, shrink from the left while the
sum is too big, and record the length when the sum is exactly right.

* Time: **O(n)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1658/v1/MinOperationsReduceX.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1658/v1/MinOperationsReduceXTest.java` | JUnit 6 tests |
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
