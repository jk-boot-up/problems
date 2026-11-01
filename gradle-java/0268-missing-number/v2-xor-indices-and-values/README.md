# 268. Missing Number — v2: XOR indices and values

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/missing-number/)

## Problem

`nums` contains `n` distinct numbers from the range `[0, n]`. Return the one number in the range that is missing.

**Example**
```
[3,0,1] → 2,   [0,1] → 2,   [9,6,4,2,3,5,7,0,1] → 8
```

**Constraints**
* `1 <= n <= 10^4`

**Follow-up:** O(1) extra space and O(n) time.

## Approach: XOR indices and values

> XOR every index and every value; all present numbers cancel, leaving the missing one.

**XOR.** Start with `x = n` and XOR in every index `i` and every value `nums[i]`. Each present number appears twice and cancels;
the missing one appears once.

* Time: **O(n)** — one pass.
* Space: **O(1)** — one accumulator.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0268/v2/MissingNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0268/v2/MissingNumberTest.java` | JUnit 6 tests |
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

* [v1-gauss-sum](../v1-gauss-sum/README.md): Gauss sum (`O(n)` time, `O(1)` space)
