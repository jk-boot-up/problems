# 2130. Maximum Twin Sum of a Linked List — v1: Reverse second half

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)

## Problem

In a linked list of even length `n`, node `i` and node `n - 1 - i` are twins. Return the maximum twin sum.

**Example**
```
5→4→2→1 → 6,   4→2→2→3 → 7,   1→100000 → 100001
```

**Constraints**
* `n` is even, `2 <= n <= 10^5`

## Approach: Reverse second half

> Reverse the second half, then walk both halves together adding twins.

**Half reversal.** Find the middle with slow/fast pointers, reverse the second half, then walk the first half and the reversed second half in
step, summing twins.

* Time: **O(n)** — a few passes.
* Space: **O(1)** — pointers only.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p2130/v1/MaximumTwinSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p2130/v1/MaximumTwinSumTest.java` | JUnit 6 tests |
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
