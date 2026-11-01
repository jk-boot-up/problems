# 747. Largest Number At Least Twice of Others — v1: Track the top two

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/largest-number-at-least-twice-of-others/)

## Problem

The largest value in `nums` is unique. Return its index if it is at least twice every other value, otherwise `-1`.

**Example**
```
[3,6,1,0] → 1,   [1,2,3,4] → -1
```

**Constraints**
* `2 <= nums.length <= 50`

## Approach: Track the top two

> Only the second-largest value needs checking: largest ≥ 2 × second largest.

**Top two.** One pass tracks the largest (and its index) and the second largest; compare `largest >= 2 × second`.

* Time: **O(n)** — one pass.
* Space: **O(1)** — three variables.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0747/v1/LargestAtLeastTwice.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0747/v1/LargestAtLeastTwiceTest.java` | JUnit 6 tests |
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
