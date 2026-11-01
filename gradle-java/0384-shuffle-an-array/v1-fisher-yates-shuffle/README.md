# 384. Shuffle an Array — v1: Fisher–Yates shuffle

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Randomized &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/shuffle-an-array/)

## Problem

Implement `ShuffleArray`:

* `ShuffleArray(int[] nums)`
* `int[] reset()` — the original array.
* `int[] shuffle()` — a random permutation; all `n!` permutations equally likely.

**Example**
```
nums = [1,2,3]
shuffle() → e.g. [3,1,2], reset() → [1,2,3], shuffle() → e.g. [1,3,2]
```

**Constraints**
* `1 <= nums.length <= 50`, values unique

## Approach: Fisher–Yates shuffle

> Fisher–Yates: fill positions from the end, each with a random pick from the not-yet-placed prefix.

**Fisher–Yates.** For `i` from `n - 1` down to 1, swap `a[i]` with `a[j]` for a uniform `j` in `0..i`. Every element is equally likely to
land in position `i`, and the rest is shuffled the same way, giving `n · (n-1) · … · 1` equally likely outcomes.

* Time: **O(n)** — per shuffle.
* Space: **O(n)** — the original copy.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0384/v1/ShuffleArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0384/v1/ShuffleArrayTest.java` | JUnit 6 tests |
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
