# 15. 3Sum

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/3sum/)

## Problem

Return all **unique** triplets `[a, b, c]` from `nums` (at different indices) with `a + b + c == 0`. The answer must not
contain duplicate triplets; order does not matter.

**Example 1**
```
Input:  nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Example 2**
```
Input:  nums = [0,1,1]
Output: []
```

**Example 3**
```
Input:  nums = [0,0,0]
Output: [[0,0,0]]
```

**Constraints**
* `3 <= nums.length <= 3000`
* `-10^5 <= nums[i] <= 10^5`

## Solutions

Each version is a separate Gradle subproject, ordered from the simplest idea to the most efficient one.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Hash set per fixed number | `O(n²)` | `O(n)` | [▶ animation](v1/animation/index.html) |
| [v2](v2/README.md) | Sort + two pointers | `O(n²)` | `O(1)` | [▶ animation](v2/animation/index.html) |

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
