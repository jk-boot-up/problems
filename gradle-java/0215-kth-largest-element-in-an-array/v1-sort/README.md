# 215. Kth Largest Element in an Array — v1: Sort

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## Problem

Return the `k`-th largest element of `nums` (in sorted order, not the k-th distinct value). Can you solve it without sorting?

**Example**
```
nums = [3,2,1,5,6,4], k = 2        → 5
nums = [3,2,3,1,2,4,5,5,6], k = 4  → 4
```

**Constraints**
* `1 <= k <= nums.length <= 10^5`; `-10^4 <= nums[i] <= 10^4`

## Approach: Sort

> Sort and read index n − k.

**Sort.** `Arrays.sort` then return `nums[n - k]`.

* Time: **O(n log n)** — sorting.
* Space: **O(log n)** — the sort's recursion stack (on a copy).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0215/v1/KthLargest.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0215/v1/KthLargestTest.java` | JUnit 6 tests |
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

* [v2-min-heap-of-size-k](../v2-min-heap-of-size-k/README.md): Min-heap of size k (`O(n log k)` time, `O(k)` space)
* [v3-quickselect](../v3-quickselect/README.md): Quickselect (`O(n)` time, `O(1)` space)
