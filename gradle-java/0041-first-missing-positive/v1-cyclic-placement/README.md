# 41. First Missing Positive — v1: Cyclic placement

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/first-missing-positive/)

## Problem

Return the smallest **positive** integer that does not appear in the unsorted array `nums`, in O(n) time and O(1) extra space.

**Example**
```
[1,2,0] → 3,   [3,4,-1,1] → 2,   [7,8,9,11,12] → 1
```

**Constraints**
* `1 <= nums.length <= 10^5`

## Approach: Cyclic placement

> Use the array itself as a hash table: put every value v in 1..n at index v − 1, then find the first misplaced slot.

**Place each value at its own index.** The answer is in `1..n+1`. For every slot, while `nums[i]` is in `1..n` and not already at
index `nums[i] - 1`, swap it there. Afterwards the first index `i` with `nums[i] != i + 1` gives the answer `i + 1`; if none, `n + 1`.

* Time: **O(n)** — every swap puts one value in its final place.
* Space: **O(1)** — the array is reused.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0041/v1/FirstMissingPositive.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0041/v1/FirstMissingPositiveTest.java` | JUnit 6 tests |
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
