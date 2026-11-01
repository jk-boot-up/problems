# 148. Sort List — v2: Bottom-up merge sort (O(1) space)

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Divide & Conquer &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/sort-list/)

## Problem

Sort a linked list in ascending order and return its head.

**Example**
```
Input:  4 → 2 → 1 → 3
Output: 1 → 2 → 3 → 4
```

**Constraints**
* `0 <= n <= 5 * 10^4`; `-10^5 <= Node.val <= 10^5`

**Follow-up:** O(n log n) time and O(1) memory.

## Approach: Bottom-up merge sort (O(1) space)

> Merge sort without recursion: merge runs of size 1, 2, 4, … across the whole list.

**Bottom-up merge sort.** For `size = 1, 2, 4, …` while `size < length`: walk the list, cut off two runs of `size` nodes, merge them, and
attach the result to the tail of the rebuilt list. No recursion, so the extra memory is constant.

* Time: **O(n log n)** — log n rounds, each a linear pass.
* Space: **O(1)** — only a few pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0148/v2/SortList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0148/v2/SortListTest.java` | JUnit 6 tests |
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

* [v1-top-down-merge-sort](../v1-top-down-merge-sort/README.md): Top-down merge sort (`O(n log n)` time, `O(log n)` space)
