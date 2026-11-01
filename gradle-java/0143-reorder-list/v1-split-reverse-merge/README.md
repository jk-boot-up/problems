# 143. Reorder List — v1: Split, reverse, merge

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reorder-list/)

## Problem

Reorder `L0 → L1 → … → Ln` into `L0 → Ln → L1 → Ln-1 → L2 → …` in place (re-link nodes, do not change values).

**Example**
```
1 → 2 → 3 → 4       becomes 1 → 4 → 2 → 3
1 → 2 → 3 → 4 → 5   becomes 1 → 5 → 2 → 4 → 3
```

**Constraints**
* `1 <= n <= 5 * 10^4`

## Approach: Split, reverse, merge

> Split at the middle, reverse the second half, then weave the two halves together.

**Three linear steps.** Find the middle with slow/fast pointers and cut the list there; reverse the second half; then alternately take one
node from each half.

* Time: **O(n)** — three passes.
* Space: **O(1)** — pointers only.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0143/v1/ReorderList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0143/v1/ReorderListTest.java` | JUnit 6 tests |
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
