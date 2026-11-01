# 206. Reverse Linked List — v2: Iterative pointer reversal

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

## Approach: Iterative pointer reversal

> Walk the list once, turning each next pointer around to point at the previous node.

**Three pointers.** Keep `prev` (already reversed part) and `cur`. Save `cur.next`, point `cur.next` at `prev`, then move both forward.

* Time: **O(n)** — each node once.
* Space: **O(1)** — three pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0206/v2/ReverseLinkedList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0206/v2/ReverseLinkedListTest.java` | JUnit 6 tests |
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

* [v1-recursive](../v1-recursive/README.md): Recursive (`O(n)` time, `O(n)` space)
