# 950. Reveal Cards In Increasing Order

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Queue &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reveal-cards-in-increasing-order/)

## Problem

A deck is revealed like this: reveal the top card and remove it, then move the next top card to the bottom; repeat until empty. Order the
deck so the cards are revealed in **increasing** order.

**Example**
```
[17,13,11,2,3,5,7] → [2,13,3,11,5,17,7]
```

**Constraints**
* `1 <= deck.length <= 1000`, distinct values

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-simulate-on-indices](v1-simulate-on-indices/README.md) | Simulate on indices | `O(n log n)` | `O(n)` | [▶ animation](v1-simulate-on-indices/animation/index.html) |
