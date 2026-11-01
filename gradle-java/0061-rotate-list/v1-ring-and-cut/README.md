# 61. Rotate List — v1: Ring and cut

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/rotate-list/)

## Problem

Rotate a linked list to the right by `k` places and return the new head.

**Example 1**
```
Input:  1 → 2 → 3 → 4 → 5, k = 2
Output: 4 → 5 → 1 → 2 → 3
```

**Example 2**
```
Input:  0 → 1 → 2, k = 4
Output: 2 → 0 → 1
```

**Constraints**
* `0 <= n <= 500`; `0 <= k <= 2 * 10^9`

## Approach: Ring and cut

> Close the list into a ring, then cut it n − k mod n nodes after the old head.

**Ring.** Find the length `n` and the tail; link the tail to the head. The new tail is `n - k % n - 1` steps from the old head; the new
head is the node after it. Break the ring there.

* Time: **O(n)** — at most two passes.
* Space: **O(1)** — pointers only.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0061/v1/RotateList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0061/v1/RotateListTest.java` | JUnit 6 tests |
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
