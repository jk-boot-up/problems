# 219. Contains Duplicate II — v1: Check the next k values

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Hashmap &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/contains-duplicate-ii/)

## Problem

Return `true` if there are two **distinct** indices `i` and `j` with `nums[i] == nums[j]` and `|i - j| <= k`.

**Example 1**
```
Input:  nums = [1,2,3,1], k = 3
Output: true
```

**Example 2**
```
Input:  nums = [1,0,1,1], k = 1
Output: true
```

**Example 3**
```
Input:  nums = [1,2,3,1,2,3], k = 2
Output: false
```

**Constraints**
* `1 <= nums.length <= 10^5`; `0 <= k <= 10^5`

## Approach: Check the next k values

> For each index, compare with the following k values.

**Bounded brute force.** For every `i`, compare `nums[i]` with `nums[i+1..i+k]`.

* Time: **O(n·k)** — up to k comparisons per index.
* Space: **O(1)** — no extra structures.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0219/v1/ContainsDuplicateII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0219/v1/ContainsDuplicateIITest.java` | JUnit 6 tests |
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

* [v2-last-index-map](../v2-last-index-map/README.md): Last-index map (`O(n)` time, `O(n)` space)
