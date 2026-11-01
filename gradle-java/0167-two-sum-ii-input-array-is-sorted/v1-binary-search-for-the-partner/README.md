# 167. Two Sum II - Input Array Is Sorted — v1: Binary search for the partner

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Problem

`numbers` is sorted in non-decreasing order (1-indexed). Find two different positions `index1 < index2` whose values add up to
`target`, and return `[index1, index2]` (1-based). Exactly one solution exists. Use only constant extra space.

**Example 1**
```
Input:  numbers = [2,7,11,15], target = 9
Output: [1,2]
```

**Example 2**
```
Input:  numbers = [-1,0], target = -1
Output: [1,2]
```

**Constraints**
* `2 <= numbers.length <= 3 * 10^4`
* `-1000 <= numbers[i], target <= 1000`

## Approach: Binary search for the partner

> For each value, binary-search the rest of the sorted array for target minus that value.

**Binary search.** For every `i`, search `numbers[i+1..n-1]` for `target - numbers[i]`.

* Time: **O(n log n)** — n binary searches.
* Space: **O(1)** — a few indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0167/v1/TwoSumII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0167/v1/TwoSumIITest.java` | JUnit 6 tests |
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

* [v2-two-pointers](../v2-two-pointers/README.md): Two pointers (`O(n)` time, `O(1)` space)
