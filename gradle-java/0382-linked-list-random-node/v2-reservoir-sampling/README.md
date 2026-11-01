# 382. Linked List Random Node — v2: Reservoir sampling

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Randomized &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/linked-list-random-node/)

## Problem

Given a singly linked list, implement `getRandom()` returning the value of a node chosen uniformly at random. Each node must be equally
likely.

* `LinkedListRandomNode(ListNode head)`
* `int getRandom()`

**Example**
```
list [1,2,3]: getRandom() returns 1, 2 or 3, each with probability 1/3
```

**Constraints**
* `1 <= n <= 10^4`; up to `10^4` calls
* Follow-up: what if the list is huge and its length unknown? Use O(1) extra space.

## Approach: Reservoir sampling

> Reservoir sampling: keep the i-th node with probability 1/i and every node ends up equally likely.

**Reservoir of size one.** Walk the list. At the `i`-th node (1-based), replace the current pick with probability `1/i`. Node `i` is
picked at step `i` with probability `1/i` and then survives every later step `j` with probability `(j-1)/j`; the product telescopes to
`1/n`. No length, no copy.

* Time: **O(n)** — per call.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0382/v2/LinkedListRandomNode.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0382/v2/LinkedListRandomNodeTest.java` | JUnit 6 tests |
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

* [v1-copy-into-an-array](../v1-copy-into-an-array/README.md): Copy into an array (`O(1)` time, `O(n)` space)
