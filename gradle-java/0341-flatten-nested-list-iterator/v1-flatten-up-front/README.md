# 341. Flatten Nested List Iterator — v1: Flatten up front

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

## Approach: Flatten up front

> Recursively copy every integer into a plain list in the constructor, then iterate over it.

**Eager flattening.** A recursive walk appends integers to a list; `next` and `hasNext` are an index into it. Simple, but it does all the
work and stores every integer before the first `next`.

* Time: **O(N)** — in the constructor, then O(1) per call.
* Space: **O(N)** — the flattened copy.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0341/v1/NestedIterator.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0341/v1/NestedIteratorTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v2-lazy-stack-of-iterators](../v2-lazy-stack-of-iterators/README.md): Lazy stack of iterators (`O(1)` time, `O(d)` space)
