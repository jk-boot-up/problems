# 649. Dota2 Senate

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Queue &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/dota2-senate/)

## Problem

Senators from parties `R` and `D` act in order, round after round. Each active senator bans one opponent from all future rounds. When only
one party has active senators, it wins. Return `"Radiant"` or `"Dire"`.

**Example**
```
"RD" → "Radiant",   "RDD" → "Dire"
```

**Constraints**
* `1 <= n <= 10^4`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-queues-by-turn-order](v1-two-queues-by-turn-order/README.md) | Two queues by turn order | `O(n)` | `O(n)` | [▶ animation](v1-two-queues-by-turn-order/animation/index.html) |
