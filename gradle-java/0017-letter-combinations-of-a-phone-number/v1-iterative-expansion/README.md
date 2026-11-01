# 17. Letter Combinations of a Phone Number — v1: Iterative expansion

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## Problem

Given a string of digits `2-9`, return all letter combinations the number could represent on a phone keypad
(`2 = abc, 3 = def, 4 = ghi, 5 = jkl, 6 = mno, 7 = pqrs, 8 = tuv, 9 = wxyz`), in any order. An empty input gives an empty list.

**Example**
```
Input:  digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Constraints**
* `0 <= digits.length <= 4`

## Approach: Iterative expansion

> Start with [""]; for each digit, extend every partial string with every letter of that digit.

**Breadth-first build.** Keep a list of partial strings; for each digit, replace the list by every partial string extended with
each of its letters.

* Time: **O(4ⁿ · n)** — the final list has up to 4ⁿ strings of length n.
* Space: **O(4ⁿ · n)** — the intermediate lists.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0017/v1/LetterCombinations.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0017/v1/LetterCombinationsTest.java` | JUnit 6 tests |
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

* [v2-backtracking](../v2-backtracking/README.md): Backtracking (`O(4ⁿ · n)` time, `O(n)` space)
