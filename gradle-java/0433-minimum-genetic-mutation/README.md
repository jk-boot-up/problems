# 433. Minimum Genetic Mutation

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

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-over-gene-strings](v1-bfs-over-gene-strings/README.md) | BFS over gene strings | `O(B·L·4)` | `O(B)` | [▶ animation](v1-bfs-over-gene-strings/animation/index.html) |
