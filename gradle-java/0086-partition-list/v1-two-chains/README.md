# 86. Partition List — v1: Two chains

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Linked List &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/partition-list/)

## Problem

Given the head of a linked list and a value `x`, rearrange it so that all nodes **less than** `x` come before nodes greater than or
equal to `x`. Keep the original relative order inside each part.

**Example 1**
```
Input:  1 → 4 → 3 → 2 → 5 → 2, x = 3
Output: 1 → 2 → 2 → 4 → 3 → 5
```

**Example 2**
```
Input:  2 → 1, x = 2
Output: 1 → 2
```

**Constraints**
* `0 <= n <= 200`; `-100 <= Node.val <= 100`; `-200 <= x <= 200`

## Approach: Two chains

> Build two chains, nodes below x and the rest, preserving order, then join them.

**Two dummy heads.** Append each node to the `less` chain or the `rest` chain. Then terminate `rest` and link `less`'s tail to `rest`'s head.

* Time: **O(n)** — one pass.
* Space: **O(1)** — nodes are re-linked, not copied.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0086/v1/PartitionList.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0086/v1/PartitionListTest.java` | JUnit 6 tests |
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
