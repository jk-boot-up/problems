# 92. Reverse Linked List II — v1: One pass, head insertion

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-linked-list-ii/)

## Problem

Given the `head` of a singly linked list and positions `left <= right` (1-based), reverse the nodes from position `left` to
`right` and return the list.

**Example 1**
```
Input:  head = 1 → 2 → 3 → 4 → 5, left = 2, right = 4
Output: 1 → 4 → 3 → 2 → 5
```

**Example 2**
```
Input:  head = 5, left = 1, right = 1
Output: 5
```

**Constraints**
* `1 <= n <= 500`; `1 <= left <= right <= n`

**Follow-up:** one pass.

## Approach: One pass, head insertion

> Walk to the node before position left, then repeatedly move the next node to the front of the sub-list.

**Head insertion.** Use a dummy node and move `prev` to the node just before `left`. Let `cur = prev.next`; `right - left` times,
take the node after `cur` and insert it right after `prev`. Each move pushes one more node to the front of the reversed part.

* Time: **O(n)** — one walk to `left`, then `right - left` constant-time moves.
* Space: **O(1)** — a few pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0092/v1/ReverseLinkedListII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0092/v1/ReverseLinkedListIITest.java` | JUnit 6 tests |
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
