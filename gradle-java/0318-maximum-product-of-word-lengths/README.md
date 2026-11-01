# 318. Maximum Product of Word Lengths

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Bit Manipulation &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-product-of-word-lengths/)

## Problem

Return the maximum value of `length(a) * length(b)` over two words of `words` that share **no** letters. Return 0 if no such pair exists.

**Example**
```
["abcw","baz","foo","bar","xtfn","abcdef"] → 16   ("abcw", "xtfn")
["a","ab","abc","d","cd","bcd","abcd"]     → 4    ("ab", "cd")
["a","aa","aaa","aaaa"]                    → 0
```

**Constraints**
* `2 <= words.length <= 1000`, lower-case words of length at most 1000

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-letter-bitmasks](v1-letter-bitmasks/README.md) | Letter bitmasks | `O(L + n²)` | `O(n)` | [▶ animation](v1-letter-bitmasks/animation/index.html) |
