# 445. Add Two Numbers II — v1: Two stacks

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-two-numbers-ii/)

## Problem

Two non-empty linked lists hold non-negative integers with the **most significant digit first**. Return their sum as a list in the same
order, without reversing the input lists.

**Example**
```
[7,2,4,3] + [5,6,4] → [7,8,0,7]    (7243 + 564 = 7807)
[2,4,3]   + [5,6,4] → [8,0,7]
[0] + [0]           → [0]
```

**Constraints**
* `1 <= length <= 100`; no leading zeros except the number 0

## Approach: Two stacks

> Digits are stored most-significant first, so push them on stacks to add from the end.

**Stacks.** Push each list's digits onto a stack, so popping yields digits from least significant. Add with a carry, and **prepend** each
result digit as a new head node, which builds the answer in the right order.

* Time: **O(m + n)**.
* Space: **O(m + n)** — the stacks.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0445/v1/AddTwoNumbersII.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0445/v1/AddTwoNumbersIITest.java` | JUnit 6 tests |
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
