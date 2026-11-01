# 19. Remove Nth Node From End of List — v2: One pass, gap of n

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

## Approach: One pass, gap of n

> Send a lead pointer n steps ahead; when it falls off the end, the trailing pointer sits just before the target.

**Two pointers with a gap.** Start `fast` and `slow` at a dummy node. Move `fast` `n + 1` steps. Then move both until `fast` is
`null`: `slow` is now just before the node to delete, so set `slow.next = slow.next.next`.

* Time: **O(L)** — one pass over the list.
* Space: **O(1)** — two pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0019/v2/RemoveNthFromEnd.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0019/v2/RemoveNthFromEndTest.java` | JUnit 6 tests |
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

* [v1-count-length-then-remove](../v1-count-length-then-remove/README.md): Count length, then remove (`O(L)` time, `O(1)` space)
