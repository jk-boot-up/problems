# 1672. Richest Customer Wealth — v1: Row sums

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Matrix &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/richest-customer-wealth/)

## Problem

`accounts[i][j]` is the money customer `i` has in bank `j`. Return the wealth (row total) of the richest customer.

**Example**
```
[[1,2,3],[3,2,1]]      → 6
[[1,5],[7,3],[3,5]]    → 10
```

**Constraints**
* `1 <= m, n <= 50`

## Approach: Row sums

> Sum each row and keep the largest.

**Row sums.** Add up each row and track the maximum.

* Time: **O(mn)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1672/v1/RichestCustomerWealth.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1672/v1/RichestCustomerWealthTest.java` | JUnit 6 tests |
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
