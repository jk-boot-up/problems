# 382. Linked List Random Node — v1: Copy into an array

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

## Approach: Copy into an array

> Store the values once; each call picks a random index.

**Array.** Copy the values into a list in the constructor. `getRandom` returns a uniformly random index's value.

* Time: **O(1)** — per call, after O(n) setup.
* Space: **O(n)** — the copy.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0382/v1/LinkedListRandomNode.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0382/v1/LinkedListRandomNodeTest.java` | JUnit 6 tests |
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

* [v2-reservoir-sampling](../v2-reservoir-sampling/README.md): Reservoir sampling (`O(n)` time, `O(1)` space)
