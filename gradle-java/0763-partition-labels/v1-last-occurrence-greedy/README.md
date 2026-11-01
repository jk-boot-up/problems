# 763. Partition Labels — v1: Last-occurrence greedy

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Greedy &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/partition-labels/)

## Problem

Split `s` into as many parts as possible so that each letter appears in at most one part. Return the part sizes in order.

**Example**
```
"ababcbacadefegdehijhklij" → [9,7,8]
"eccbbbbdec"               → [10]
```

**Constraints**
* `1 <= s.length <= 500`; lowercase letters.

## Approach: Last-occurrence greedy

> A part must extend at least to the last occurrence of every letter it contains; cut as soon as that reach is met.

**Reach.** Record each letter's last index. Scan, extending `end = max(end, last[c])`; when `i == end`, the part is closed.

* Time: **O(n)** — two passes.
* Space: **O(1)** — 26 last indices.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0763/v1/PartitionLabels.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0763/v1/PartitionLabelsTest.java` | JUnit 6 tests |
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
