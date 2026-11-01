# 307. Range Sum Query - Mutable — v2: Fenwick (binary indexed) tree

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Fenwick Tree &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/range-sum-query-mutable/)

## Problem

Implement `NumArray` supporting both updates and range sums:

* `NumArray(int[] nums)`
* `void update(int index, int val)` — set `nums[index] = val`.
* `int sumRange(int left, int right)` — the sum of `nums[left..right]`.

**Example**
```
nums = [1,3,5]
sumRange(0,2) → 9, update(1,2), sumRange(0,2) → 8
```

**Constraints**
* `1 <= nums.length <= 3 * 10^4`, up to `3 * 10^4` calls

## Approach: Fenwick (binary indexed) tree

> A Fenwick tree stores partial sums over power-of-two blocks, so both update and prefix sum take log n steps.

**Fenwick tree.** Slot `i` (1-based) stores the sum of the `i & -i` elements ending at `i`. A prefix sum walks `i -= i & -i`, collecting
at most `log n` slots; an update by `delta` walks `i += i & -i`, touching every slot that covers that index. A range sum is the difference
of two prefix sums. Keep a copy of the values to turn `update` into a delta.

* Time: **O(log n)** — per update or query.
* Space: **O(n)** — the tree.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0307/v2/NumArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0307/v2/NumArrayTest.java` | JUnit 6 tests |
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

* [v1-plain-array-sum-on-demand](../v1-plain-array-sum-on-demand/README.md): Plain array, sum on demand (`O(n)` time, `O(n)` space)
