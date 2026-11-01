# 1929. Concatenation of Array — v1: Write both copies

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/concatenation-of-array/)

## Problem

Return `ans` of length `2n` with `ans[i] = ans[i + n] = nums[i]`.

**Example**
```
[1,2,1]   → [1,2,1,1,2,1]
[1,3,2,1] → [1,3,2,1,1,3,2,1]
```

**Constraints**
* `1 <= n <= 1000`

## Approach: Write both copies

> Write each element twice: at i and at i + n.

**Two writes per element.** Fill `ans[i]` and `ans[i + n]` in one loop.

* Time: **O(n)**.
* Space: **O(n)** — the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1929/v1/ConcatenationOfArray.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1929/v1/ConcatenationOfArrayTest.java` | JUnit 6 tests |
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
