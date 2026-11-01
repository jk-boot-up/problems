# 299. Bulls and Cows

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Hash Map &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/bulls-and-cows/)

## Problem

Given a `secret` and a `guess` of the same length (digits only), return the hint `"xAyB"`: `x` **bulls** (right digit, right position)
and `y` **cows** (digits in the guess that are in the secret but in the wrong position, each secret digit used at most once).

**Example**
```
secret = "1807", guess = "7810" → "1A3B"
secret = "1123", guess = "0111" → "1A1B"
```

**Constraints**
* `1 <= length <= 1000`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-one-pass-with-a-signed-tally](v1-one-pass-with-a-signed-tally/README.md) | One pass with a signed tally | `O(n)` | `O(1)` | [▶ animation](v1-one-pass-with-a-signed-tally/animation/index.html) |
