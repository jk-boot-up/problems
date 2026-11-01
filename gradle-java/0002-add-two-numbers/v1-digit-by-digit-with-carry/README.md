# 2. Add Two Numbers — v1: Digit-by-digit with carry

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/add-two-numbers/)

## Problem

Two non-negative integers are stored as linked lists with their digits in **reverse order** (ones digit first), one digit per node.
Return their sum as a linked list in the same format. Neither number has leading zeros, except the number 0 itself.

**Example 1**
```
Input:  l1 = 2 → 4 → 3, l2 = 5 → 6 → 4    (342 + 465)
Output: 7 → 0 → 8                         (807)
```

**Example 2**
```
Input:  l1 = 9 → 9 → 9 → 9, l2 = 9 → 9
Output: 8 → 9 → 0 → 0 → 1
```

**Constraints**
* Each list has `1..100` nodes; `0 <= Node.val <= 9`.

## Approach: Digit-by-digit with carry

> Digits are stored lowest first, so add them pairwise like on paper, carrying into the next node.

**Schoolbook addition.** Walk both lists together; `sum = x + y + carry`, emit `sum % 10`, carry `sum / 10`. Continue while
either list has nodes or a carry remains. A dummy head keeps the code simple.

* Time: **O(max(m, n))** — one step per digit.
* Space: **O(1)** — apart from the output list.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0002/v1/AddTwoNumbers.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0002/v1/AddTwoNumbersTest.java` | JUnit 6 tests |
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
