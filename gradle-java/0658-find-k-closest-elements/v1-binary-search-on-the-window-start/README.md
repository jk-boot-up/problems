# 658. Find K Closest Elements — v1: Binary search on the window start

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Binary Search &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-k-closest-elements/)

## Problem

Given a sorted array, return the `k` elements closest to `x`, in ascending order. `a` is closer than `b` if `|a - x| < |b - x|`, or equal
distance and `a < b`.

**Example**
```
arr = [1,2,3,4,5], k = 4, x = 3  → [1,2,3,4]
arr = [1,1,2,3,4,5], k = 4, x = -1 → [1,1,2,3]
```

**Constraints**
* `1 <= k <= arr.length <= 10^4`

## Approach: Binary search on the window start

> Binary-search the left edge of the k-length window: compare the distances of x to arr[mid] and arr[mid + k].

**Search the start.** The answer is a contiguous window `[lo, lo + k)`. For a candidate `mid`, if `x - arr[mid] > arr[mid + k] - x`, the
window should move right; otherwise left (ties keep the smaller values).

* Time: **O(log(n − k) + k)** — the search plus building the output.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0658/v1/FindKClosestElements.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0658/v1/FindKClosestElementsTest.java` | JUnit 6 tests |
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
