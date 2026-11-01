# 341. Flatten Nested List Iterator — v2: Lazy stack of iterators

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

## Approach: Lazy stack of iterators

> Keep a stack of iterators; dive into lists lazily and only stop when an integer is on top.

**Stack of iterators.** Push an iterator over the top-level list. `hasNext` does the real work: while no integer is ready, look at the top
iterator. If it is exhausted, pop it; if its next item is a list, push that list's iterator; if it is an integer, keep it ready. Empty
lists simply get popped. `next` returns the ready integer.

* Time: **O(1)** amortised — each item and each list is visited once over the whole iteration.
* Space: **O(d)** — one iterator per nesting level.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0341/v2/NestedIterator.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0341/v2/NestedIteratorTest.java` | JUnit 6 tests |
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

* [v1-flatten-up-front](../v1-flatten-up-front/README.md): Flatten up front (`O(N)` time, `O(N)` space)
