# 283. Move Zeroes — v1: Swap with write pointer

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Two Pointers &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/move-zeroes/)

## Problem

Move all `0`s in `nums` to the end **in place**, keeping the relative order of the non-zero values.

**Example**
```
[0,1,0,3,12] → [1,3,12,0,0]
```

**Constraints**
* `1 <= nums.length <= 10^4`

## Approach: Swap with write pointer

> Swap each non-zero value forward to the write pointer; zeros drift to the back.

**Read/write pointers.** `k` is where the next non-zero belongs. For each non-zero `nums[i]`, swap it with `nums[k]` and advance `k`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — in place.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0283/v1/MoveZeroes.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0283/v1/MoveZeroesTest.java` | JUnit 6 tests |
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
