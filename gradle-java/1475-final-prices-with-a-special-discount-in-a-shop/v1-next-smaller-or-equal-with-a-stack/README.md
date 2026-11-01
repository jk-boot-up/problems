# 1475. Final Prices With a Special Discount in a Shop — v1: Next smaller-or-equal with a stack

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Monotonic Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)

## Problem

Item `i` costs `prices[i]`. Its discount is `prices[j]` for the **first** `j > i` with `prices[j] <= prices[i]` (no discount if none).
Return the final prices.

**Example**
```
[8,4,6,2,3] → [4,2,4,2,3]
[1,2,3,4,5] → [1,2,3,4,5]
[10,1,1,6]  → [9,0,1,6]
```

**Constraints**
* `1 <= prices.length <= 500`

## Approach: Next smaller-or-equal with a stack

> Each item's discount is the next item to its right that costs no more; a monotonic stack finds all of them in one pass.

**Pending items.** Keep a stack of indices still waiting for their discount (their prices increase up the stack). When a new price is `<=`
the price on top, that top item gets this discount: pop it and subtract. Then push the new index.

* Time: **O(n)**.
* Space: **O(n)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1475/v1/FinalPrices.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1475/v1/FinalPricesTest.java` | JUnit 6 tests |
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
