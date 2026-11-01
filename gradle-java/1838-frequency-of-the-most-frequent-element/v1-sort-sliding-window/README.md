# 1838. Frequency of the Most Frequent Element — v1: Sort + sliding window

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

## Problem

In one operation you may increase any element by 1. With at most `k` operations, return the largest possible frequency of a single value.

**Example**
```
nums = [1,2,4],    k = 5 → 3   (raise 1 and 2 to 4)
nums = [1,4,8,13], k = 5 → 2
nums = [3,9,6],    k = 2 → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^5`, `1 <= k <= 10^5`

## Approach: Sort + sliding window

> Sort; a window can all be raised to its largest value if largest × length − window sum ≤ k.

**Raise to the right end.** Only increases are allowed, so the target value should be an existing element and the elements raised to it
should be the closest smaller ones. After sorting, a window `[lo, hi]` can be made all equal to `nums[hi]` at a cost of
`nums[hi] · len - sum`. Grow `hi`; shrink `lo` while the cost exceeds `k`. Use `long` for the product.

* Time: **O(n log n)** — sorting.
* Space: **O(1)** — besides sorting.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1838/v1/MostFrequentAfterIncrements.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1838/v1/MostFrequentAfterIncrementsTest.java` | JUnit 6 tests |
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
