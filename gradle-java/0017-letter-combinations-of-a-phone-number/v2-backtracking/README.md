# 17. Letter Combinations of a Phone Number — v2: Backtracking

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

## Approach: Backtracking

> Choose one letter per digit, depth by depth; each complete choice is one combination.

**Backtracking.** At depth `i`, try each letter for `digits[i]`, append it, recurse to depth `i + 1`, then remove it. At depth
`digits.length` the builder holds a full combination.

* Time: **O(4ⁿ · n)** — up to 4 letters per digit, and each of the up to 4ⁿ results costs O(n) to copy.
* Space: **O(n)** — the recursion depth and builder (plus the output).

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0017/v2/LetterCombinations.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0017/v2/LetterCombinationsTest.java` | JUnit 6 tests |
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

* [v1-iterative-expansion](../v1-iterative-expansion/README.md): Iterative expansion (`O(4ⁿ · n)` time, `O(4ⁿ · n)` space)
