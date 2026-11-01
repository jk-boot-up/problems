# 328. Odd Even Linked List — v1: Two interleaved chains

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/odd-even-linked-list/)

## Problem

Group all nodes at **odd positions** (1st, 3rd, …) first, followed by nodes at even positions, keeping relative order within each group.
Use O(1) extra space and O(n) time.

**Example**
```
1 → 2 → 3 → 4 → 5        becomes 1 → 3 → 5 → 2 → 4
2 → 1 → 3 → 5 → 6 → 4 → 7 becomes 2 → 3 → 6 → 7 → 1 → 5 → 4
```

**Constraints**
* `0 <= n <= 10^4`

## Approach: Two interleaved chains

> Build the odd-position chain and the even-position chain in one pass, then attach evens after odds.

**Leapfrog.** `odd` and `even` walk two steps at a time, each skipping over the other's nodes: `odd.next = even.next`,
`even.next = odd.next`. Finally link the odd tail to the saved even head.

* Time: **O(n)** — one pass.
* Space: **O(1)** — pointers only.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0328/v1/OddEvenLinkedList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0328/v1/OddEvenLinkedListTest.java` | JUnit 6 tests |
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
