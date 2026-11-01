# 278. First Bad Version — v1: Binary search for the boundary

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/first-bad-version/)

## Problem

Versions `1..n` were released in order. Once a version is bad, every later version is bad too. Given an API `isBadVersion(v)`, find the
first bad version while calling the API as few times as possible.

In this project the API is passed to the constructor as an `IntPredicate`.

**Example**
```
n = 5, first bad = 4 → 4   (isBad(3) = false, isBad(5) = true, isBad(4) = true)
n = 1, first bad = 1 → 1
```

**Constraints**
* `1 <= bad <= n <= 2^31 - 1`

## Approach: Binary search for the boundary

> Bad versions form a suffix; binary search for where the suffix starts.

**Lower bound.** Keep `lo..hi` containing the answer. Test the middle: if it is bad, the answer is at `mid` or to its left (`hi = mid`);
otherwise it is to the right (`lo = mid + 1`). Compute `mid = lo + (hi - lo) / 2` so `lo + hi` cannot overflow.

* Time: **O(log n)** — about 31 API calls at most.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0278/v1/FirstBadVersion.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0278/v1/FirstBadVersionTest.java` | JUnit 6 tests |
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
