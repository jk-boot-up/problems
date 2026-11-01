# 284. Peeking Iterator

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/peeking-iterator/)

## Problem

Wrap an `Iterator<Integer>` in a `PeekingIterator` that also supports `peek()`, which returns the next element **without** advancing.

* `PeekingIterator(Iterator<Integer> it)`
* `Integer next()`, `boolean hasNext()`, `Integer peek()`

**Example**
```
iterator over [1,2,3]
next() → 1, peek() → 2, next() → 2, next() → 3, hasNext() → false
```

**Constraints**
* `1 <= length <= 1000`; `next` and `peek` are only called when an element remains

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-cache-the-next-element](v1-cache-the-next-element/README.md) | Cache the next element | `O(1)` | `O(1)` | [▶ animation](v1-cache-the-next-element/animation/index.html) |
