# 682. Baseball Game

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/baseball-game/)

## Problem

Process operations: an integer records that score; `"+"` records the sum of the previous two scores; `"D"` records double the previous score;
`"C"` removes the previous score. Return the sum of the remaining scores.

**Example**
```
["5","2","C","D","+"] → 30,   ["5","-2","4","C","D","9","+","+"] → 27
```

**Constraints**
* `1 <= operations.length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-score-stack](v1-score-stack/README.md) | Score stack | `O(n)` | `O(n)` | [▶ animation](v1-score-stack/animation/index.html) |
