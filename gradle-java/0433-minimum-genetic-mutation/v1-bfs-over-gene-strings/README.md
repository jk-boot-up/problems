# 433. Minimum Genetic Mutation — v1: BFS over gene strings

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-genetic-mutation/)

## Problem

A gene is an 8-character string over `A, C, G, T`. A mutation changes one character, and every intermediate gene must be in `bank`.
Return the minimum number of mutations from `startGene` to `endGene`, or `-1` if impossible. `startGene` may not be in the bank.

**Example**
```
Input:  startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
```

**Constraints**
* `0 <= bank.length <= 10`; all strings have length 8.

## Approach: BFS over gene strings

> Genes are nodes; one-letter changes that land in the bank are edges; BFS gives the fewest mutations.

**BFS.** Put the bank in a `MyHashSet`. From each gene, try all `8 × 3` single-letter changes; any change that is in the bank and not
yet visited joins the next level.

* Time: **O(B·L·4)** — each bank gene is expanded once, trying 4 letters at each of L = 8 positions.
* Space: **O(B)** — the bank set and the queue.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0433/v1/MinimumGeneticMutation.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0433/v1/MinimumGeneticMutationTest.java` | JUnit 6 tests |
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
