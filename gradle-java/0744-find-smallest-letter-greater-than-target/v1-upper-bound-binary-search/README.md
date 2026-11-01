# 744. Find Smallest Letter Greater Than Target — v1: Upper-bound binary search

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

## Problem

`letters` is sorted (non-decreasing) and contains at least two different letters. Return the smallest letter strictly greater than `target`,
or `letters[0]` if none is.

**Example**
```
letters = [c,f,j], target = a → c;  target = c → f;  letters = [x,x,y,y], target = z → x
```

**Constraints**
* `2 <= letters.length <= 10^4`

## Approach: Upper-bound binary search

> Binary-search the first letter strictly greater than the target; wrap around to the first letter if none.

**Upper bound.** Find the first index with `letters[i] > target`; if it is `n`, wrap to 0.

* Time: **O(log n)** — binary search.
* Space: **O(1)** — two indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0744/v1/SmallestLetterGreaterThanTarget.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0744/v1/SmallestLetterGreaterThanTargetTest.java` | JUnit 6 tests |
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
