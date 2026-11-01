# 142. Linked List Cycle II — v2: Floyd: meet, then find the entrance

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/)

## Problem

Return the node where the cycle in a linked list begins, or `null` if there is no cycle. Do not modify the list.

**Example**
```
3 → 2 → 0 → -4 → (back to 2)   → the node with value 2
1 → 2 → (back to 1)            → the node with value 1
```

**Constraints**
* `0 <= n <= 10^4`

**Follow-up:** O(1) memory.

## Approach: Floyd: meet, then find the entrance

> After slow and fast meet, a pointer from the head and one from the meeting point reach the cycle start together.

**Floyd's algorithm, phase 2.** Let `a` be the distance from the head to the cycle start. When slow and fast meet, slow has walked
`a + b`, fast `2(a + b)`, so `a + b` is a multiple of the cycle length. Walking `a` more steps from the meeting point therefore lands on
the cycle start, exactly when a pointer from the head gets there.

* Time: **O(n)** — two linear phases.
* Space: **O(1)** — two pointers.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0142/v2/LinkedListCycleII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0142/v2/LinkedListCycleIITest.java` | JUnit 6 tests |
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

* [v1-visited-node-set](../v1-visited-node-set/README.md): Visited-node set (`O(n)` time, `O(n)` space)
