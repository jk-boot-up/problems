# 19. Remove Nth Node From End of List — v1: Count length, then remove

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## Problem

Remove the `n`-th node from the **end** of the list and return its head.

**Example 1**
```
Input:  head = 1 → 2 → 3 → 4 → 5, n = 2
Output: 1 → 2 → 3 → 5
```

**Example 2**
```
Input:  head = 1, n = 1
Output: (empty)
```

**Constraints**
* `1 <= sz <= 30`; `1 <= n <= sz`

**Follow-up:** one pass.

## Approach: Count length, then remove

> First count the nodes, then walk to position length − n.

**Two passes.** Count the length `L`. The node to remove is at index `L - n`; walk `L - n` steps from a dummy and unlink the next node.

* Time: **O(L)** — two passes.
* Space: **O(1)** — a counter and a pointer.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0019/v1/RemoveNthFromEnd.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0019/v1/RemoveNthFromEndTest.java` | JUnit 6 tests |
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

* [v2-one-pass-gap-of-n](../v2-one-pass-gap-of-n/README.md): One pass, gap of n (`O(L)` time, `O(1)` space)
