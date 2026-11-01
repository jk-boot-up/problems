# 284. Peeking Iterator — v1: Cache the next element

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

## Approach: Cache the next element

> Read one element ahead and keep it in a field; peek returns it, next hands it over and reads the next one.

**One element of look-ahead.** In the constructor, pull the first element (if any) into `ahead`. `peek` returns `ahead`. `next` returns
`ahead` and refills it from the inner iterator. A separate flag, not `null`, records whether `ahead` is valid.

* Time: **O(1)** — per call.
* Space: **O(1)** — one cached element.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0284/v1/PeekingIterator.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0284/v1/PeekingIteratorTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
