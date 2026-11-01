# 386. Lexicographical Numbers — v1: Iterative pre-order walk

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Trie &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/lexicographical-numbers/)

## Problem

Return the numbers `1..n` sorted in **lexicographical** (dictionary) order, in O(n) time and O(1) extra space.

**Example**
```
n = 13 → [1,10,11,12,13,2,3,4,5,6,7,8,9]
n = 2  → [1,2]
```

**Constraints**
* `1 <= n <= 5 * 10^4`

## Approach: Iterative pre-order walk

> Walk the implicit 10-ary trie in pre-order: go deeper by ×10, otherwise step to the next sibling.

**Pre-order of a digit trie.** After `cur`, the next number in dictionary order is `cur * 10` if that is `<= n` (go to the first child).
Otherwise go to the next sibling `cur + 1`; but first climb up (`cur /= 10`) while `cur` ends in 9 or `cur + 1 > n`, since those have no
next sibling at this level.

* Time: **O(n)** — each step moves along the trie a bounded amortised amount.
* Space: **O(1)** — besides the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0386/v1/LexicographicalNumbers.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0386/v1/LexicographicalNumbersTest.java` | JUnit 6 tests |
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
