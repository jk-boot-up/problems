# 46. Permutations — v2: In-place swapping

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/permutations/)

## Problem

Given an array `nums` of **distinct** integers, return all possible permutations, in any order.

**Example**
```
Input:  nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
```

**Constraints**
* `1 <= nums.length <= 6`; values are distinct.

## Approach: In-place swapping

> Fix positions left to right by swapping each remaining value into the current position.

**Swap into place.** `permute(i)`: positions `0..i-1` are fixed. For each `j >= i`, swap `nums[i]` and `nums[j]`, recurse with `i + 1`,
then swap back. At `i == n`, record the array.

* Time: **O(n · n!)** — n! permutations, each copied in O(n).
* Space: **O(n)** — the recursion depth (no "used" array needed).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0046/v2/Permutations.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0046/v2/PermutationsTest.java` | JUnit 6 tests |
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

* [v1-path-with-used-flags](../v1-path-with-used-flags/README.md): Path with used flags (`O(n · n!)` time, `O(n)` space)
