# 394. Decode String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/decode-string/)

## Problem

Decode a string encoded as `k[encoded]`, meaning `encoded` repeated `k` times. Encodings may be nested; digits only appear as repeat counts.

**Example**
```
"3[a]2[bc]" → "aaabcbc",   "3[a2[c]]" → "accaccacc",   "2[abc]3[cd]ef" → "abcabccdcdcdef"
```

**Constraints**
* `1 <= s.length <= 30`; output length at most `10^5`.

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-two-stacks](v1-two-stacks/README.md) | Two stacks | `O(output)` | `O(output)` | [▶ animation](v1-two-stacks/animation/index.html) |
