# 220. Contains Duplicate III — v1: Check every nearby pair

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contains-duplicate-iii/)

## Problem

Given `nums`, `indexDiff` and `valueDiff`, return `true` if there are two indices `i != j` with `|i - j| <= indexDiff` and
`|nums[i] - nums[j]| <= valueDiff`.

**Example**
```
nums = [1,2,3,1],     indexDiff = 3, valueDiff = 0 → true
nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3 → false
```

**Constraints**
* `2 <= nums.length <= 10^5`, `-10^9 <= nums[i] <= 10^9`, `1 <= indexDiff <= nums.length`, `0 <= valueDiff <= 10^9`

## Approach: Check every nearby pair

> For each index, compare it with the next indexDiff elements.

**Brute force.** For each `i`, compare `nums[i]` with `nums[i+1..i+indexDiff]` using `long` differences.

* Time: **O(n · k)** — `k = indexDiff` comparisons per element.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0220/v1/ContainsDuplicateIII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0220/v1/ContainsDuplicateIIITest.java` | JUnit 6 tests |
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

* [v2-ordered-window-with-treeset](../v2-ordered-window-with-treeset/README.md): Ordered window with TreeSet (`O(n log k)` time, `O(k)` space)
* [v3-buckets-over-a-sliding-window](../v3-buckets-over-a-sliding-window/README.md): Buckets over a sliding window (`O(n)` time, `O(min(n, k))` space)
