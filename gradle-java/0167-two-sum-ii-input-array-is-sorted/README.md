# 167. Two Sum II - Input Array Is Sorted

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

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Binary search for the partner | `O(n log n)` | `O(1)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Two pointers | `O(n)` | `O(1)` | [▶ animation](v2/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
