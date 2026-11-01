# 206. Reverse Linked List — v1: Recursive

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-linked-list/)

## Problem

Reverse a singly linked list and return the new head.

**Example**
```
1 → 2 → 3 → 4 → 5   becomes   5 → 4 → 3 → 2 → 1
```

**Constraints**
* `0 <= n <= 5000`

**Follow-up:** do it both iteratively and recursively.

## Approach: Recursive

> Reverse the rest of the list, then hook the current node onto its end.

**Recursion.** `reverse(head)`: reverse `head.next`, then `head.next.next = head` and `head.next = null`.

* Time: **O(n)** — one call per node.
* Space: **O(n)** — the recursion stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0206/v1/ReverseLinkedList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0206/v1/ReverseLinkedListTest.java` | JUnit 6 tests |
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

* [v2-iterative-pointer-reversal](../v2-iterative-pointer-reversal/README.md): Iterative pointer reversal (`O(n)` time, `O(1)` space)
