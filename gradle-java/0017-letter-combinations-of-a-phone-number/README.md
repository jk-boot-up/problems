# 17. Letter Combinations of a Phone Number

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

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-iterative-expansion](v1-iterative-expansion/README.md) | Iterative expansion | `O(4ⁿ · n)` | `O(4ⁿ · n)` | [▶ animation](v1-iterative-expansion/animation/index.html) |
| [v2-backtracking](v2-backtracking/README.md) | Backtracking | `O(4ⁿ · n)` | `O(n)` | [▶ animation](v2-backtracking/animation/index.html) |
