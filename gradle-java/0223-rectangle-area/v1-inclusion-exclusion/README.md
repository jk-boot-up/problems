# 223. Rectangle Area — v1: Inclusion–exclusion

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rectangle-area/)

## Problem

Two axis-aligned rectangles are given by their bottom-left `(ax1, ay1)`, `(bx1, by1)` and top-right `(ax2, ay2)`, `(bx2, by2)` corners.
Return the total area they cover.

**Example**
```
ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2 → 45
ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2 → 16
```

**Constraints**
* `-10^4 <= all coordinates <= 10^4`

## Approach: Inclusion–exclusion

> Add both areas and subtract the overlap, whose sides are clamped at zero.

**Inclusion–exclusion.** The overlap is a rectangle from `max` of the left/bottom edges to `min` of the right/top edges. Its width and
height are clamped at 0 when the rectangles do not meet. Answer: `areaA + areaB - overlap`.

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0223/v1/RectangleArea.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0223/v1/RectangleAreaTest.java` | JUnit 6 tests |
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
