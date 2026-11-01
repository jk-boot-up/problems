# 1721. Swapping Nodes in a Linked List — v1: Two pointers, swap values

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)

## Problem

Swap the **values** of the `k`-th node from the beginning and the `k`-th node from the end (1-indexed) and return the head.

**Example**
```
head = [1,2,3,4,5], k = 2 → [1,4,3,2,5]
head = [7,9,6,6,7,8,3,0,9,5], k = 5 → [7,9,6,6,8,7,3,0,9,5]
```

**Constraints**
* `1 <= k <= n <= 10^5`

## Approach: Two pointers, swap values

> Walk k − 1 steps to find the k-th node; a second pointer started at the head reaches the k-th from the end when the first one falls off.

**Gap of k.** Move `fast` to the `k`-th node and remember it as `first`. Then move `fast` and `slow` (from the head) together until `fast`
is the last node; `slow` is now the `k`-th from the end. Swap the two values.

* Time: **O(n)** — one pass.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1721/v1/SwapNodesInList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1721/v1/SwapNodesInListTest.java` | JUnit 6 tests |
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
