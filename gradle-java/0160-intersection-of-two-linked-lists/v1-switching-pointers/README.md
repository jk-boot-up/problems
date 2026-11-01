# 160. Intersection of Two Linked Lists — v1: Switching pointers

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/intersection-of-two-linked-lists/)

## Problem

Two singly linked lists may merge into a shared tail. Return the first shared **node**, or `null` if they do not intersect. Do not modify
the lists.

**Example**
```
A: 4 → 1 ↘
            8 → 4 → 5
B: 5 → 6 → 1 ↗          → the node with value 8
```

**Constraints**
* `1 <= m, n <= 3 * 10^4`

**Follow-up:** O(m + n) time and O(1) memory.

## Approach: Switching pointers

> Two pointers walk A then B and B then A; after equal total distances they meet at the intersection (or both reach null).

**Equalize the distances.** `p` walks A then B; `q` walks B then A. Each travels `a + c + b` steps before reaching the intersection
(where `c` is the shared length), so they arrive together, or both reach `null` if there is no intersection.

* Time: **O(m + n)** — each pointer walks both lists once.
* Space: **O(1)** — two pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0160/v1/IntersectionOfTwoLists.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0160/v1/IntersectionOfTwoListsTest.java` | JUnit 6 tests |
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
