# 901. Online Stock Span — v1: Monotonic stack with spans

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

## Approach: Monotonic stack with spans

> A stack of (price, span) pairs; a new price absorbs every smaller-or-equal price on top, adding their spans.

**Collapse smaller days.** Keep a decreasing stack of `(price, span)`. For a new price, pop every entry with price `<=` it and add its span to
today's span; push the result.

* Time: **O(1)** — amortized per call (each day is pushed and popped once).
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0901/v1/StockSpanner.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0901/v1/StockSpannerTest.java` | JUnit 6 tests |
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
