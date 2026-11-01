# 341. Flatten Nested List Iterator

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/flatten-nested-list-iterator/)

## Problem

A nested list holds integers or other nested lists. Implement an iterator over all of its integers, in order.

* `NestedIterator(List<NestedInteger> nestedList)`
* `int next()`, `boolean hasNext()`

`NestedInteger` (provided in this project) has `isInteger()`, `getInteger()` and `getList()`.

**Example**
```
[[1,1],2,[1,1]] → 1,1,2,1,1
[1,[4,[6]]]     → 1,4,6
[[],[[]]]       → (nothing)
```

**Constraints**
* Up to 500 elements; integers in `[-10^6, 10^6]`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-flatten-up-front](v1-flatten-up-front/README.md) | Flatten up front | `O(N)` | `O(N)` | [▶ animation](v1-flatten-up-front/animation/index.html) |
| [v2-lazy-stack-of-iterators](v2-lazy-stack-of-iterators/README.md) | Lazy stack of iterators | `O(1)` | `O(d)` | [▶ animation](v2-lazy-stack-of-iterators/animation/index.html) |
