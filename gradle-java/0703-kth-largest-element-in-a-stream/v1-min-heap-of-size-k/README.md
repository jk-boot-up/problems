# 703. Kth Largest Element in a Stream — v1: Min-heap of size k

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Heap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

## Problem

Implement `KthLargest(k, nums)` and `int add(val)`, which adds `val` to the stream and returns the current `k`-th largest element.

**Example**
```
KthLargest(3, [4,5,8,2]); add(3) → 4; add(5) → 5; add(10) → 5; add(9) → 8; add(4) → 8
```

**Constraints**
* `1 <= k <= 10^4`; at least `k` elements exist when `add` returns.

## Approach: Min-heap of size k

> A min-heap of size k keeps the k largest scores; its top is the k-th largest.

**Bounded heap.** Keep only the `k` largest values in a min-heap; after each add, pop while the size exceeds `k`. The top is the answer.

* Time: **O(log k)** — per add.
* Space: **O(k)** — the heap.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0703/v1/KthLargestInStream.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0703/v1/KthLargestInStreamTest.java` | JUnit 6 tests |
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
