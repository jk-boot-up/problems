# 234. Palindrome Linked List — v1: Reverse second half

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/palindrome-linked-list/)

## Problem

Return `true` if a singly linked list reads the same forward and backward.

**Example**
```
1 → 2 → 2 → 1 → true,   1 → 2 → false
```

**Constraints**
* `1 <= n <= 10^5`

**Follow-up:** O(n) time and O(1) space.

## Approach: Reverse second half

> Reverse the second half in place and compare it with the first half.

**Half reversal.** Find the middle with slow/fast pointers, reverse the second half, then walk both halves comparing values.

* Time: **O(n)** — a few linear passes.
* Space: **O(1)** — pointers only.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0234/v1/PalindromeLinkedList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0234/v1/PalindromeLinkedListTest.java` | JUnit 6 tests |
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
