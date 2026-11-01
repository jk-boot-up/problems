# 179. Largest Number — v1: Sort by concatenation order

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Sorting &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/largest-number/)

## Problem

Given non-negative integers `nums`, arrange them so they form the largest possible number, and return it as a string.

**Example**
```
[10,2]          → "210"
[3,30,34,5,9]   → "9534330"
[0,0]           → "0"
```

**Constraints**
* `1 <= nums.length <= 100`, `0 <= nums[i] <= 10^9`

## Approach: Sort by concatenation order

> Put a before b exactly when the string a+b beats b+a.

**Custom order.** Compare two numbers by trying both orders: `a` goes first if `a + b > b + a` as strings. This order is transitive, so a
normal sort produces the best arrangement. If the biggest piece is `"0"`, every piece is zero: return `"0"`, not `"00"`.

* Time: **O(n log n · L)** — sorting with comparisons of length `L` (at most 20 characters).
* Space: **O(n · L)** — the strings.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0179/v1/LargestNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0179/v1/LargestNumberTest.java` | JUnit 6 tests |
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
