# 752. Open the Lock

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Graph BFS &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/open-the-lock/)

## Problem

A lock has 4 wheels with digits 0–9; one move turns one wheel one step up or down (wrapping 9 ↔ 0). It starts at `"0000"`. Some
combinations are **deadends** that jam the lock. Return the fewest moves to reach `target`, or `-1`.

**Example**
```
deadends = ["0201","0101","0102","1212","2002"], target = "0202" → 6
deadends = ["8888"], target = "0009" → 1
```

**Constraints**
* `1 <= deadends.length <= 500`; all strings have 4 digits

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-bfs-over-combinations](v1-bfs-over-combinations/README.md) | BFS over combinations | `O(10⁴ · 8 · 4)` | `O(10⁴)` | [▶ animation](v1-bfs-over-combinations/animation/index.html) |
