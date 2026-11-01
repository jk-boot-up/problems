# 901. Online Stock Span

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/online-stock-span/)

## Problem

Implement `StockSpanner.next(price)`: return today's **span**, the number of consecutive days (ending today, going backward) with a price
at most today's price.

**Example**
```
next(100)=1, next(80)=1, next(60)=1, next(70)=2, next(60)=1, next(75)=4, next(85)=6
```

**Constraints**
* At most `10^4` calls.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-monotonic-stack-with-spans](v1-monotonic-stack-with-spans/README.md) | Monotonic stack with spans | `O(1)` | `O(n)` | [▶ animation](v1-monotonic-stack-with-spans/animation/index.html) |
