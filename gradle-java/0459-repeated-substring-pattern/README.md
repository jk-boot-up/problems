# 459. Repeated Substring Pattern

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/repeated-substring-pattern/)

## Problem

Return `true` if `s` can be built by repeating one of its substrings two or more times.

**Example**
```
"abab"         → true   ("ab" × 2)
"aba"          → false
"abcabcabcabc" → true
```

**Constraints**
* `1 <= s.length <= 10^4`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-doubled-string-trick](v1-doubled-string-trick/README.md) | Doubled-string trick | `O(n²)` | `O(n)` | [▶ animation](v1-doubled-string-trick/animation/index.html) |
| [v2-kmp-prefix-function](v2-kmp-prefix-function/README.md) | KMP prefix function | `O(n)` | `O(n)` | [▶ animation](v2-kmp-prefix-function/animation/index.html) |
