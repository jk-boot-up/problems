# 151. Reverse Words in a String

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/)

## Problem

Given a string `s`, reverse the order of its **words**. A word is a run of non-space characters. The result must have exactly
one space between words and no leading or trailing spaces, even if `s` has extra spaces.

**Example 1**
```
Input:  s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2**
```
Input:  s = "  hello world  "
Output: "world hello"
```

**Example 3**
```
Input:  s = "a good   example"
Output: "example good a"
```

**Constraints**
* `1 <= s.length <= 10^4`; letters, digits and spaces; at least one word.

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-split-reverse-join](v1-split-reverse-join/README.md) | Split, reverse, join | `O(n)` | `O(n)` | [▶ animation](v1-split-reverse-join/animation/index.html) |
| [v2-manual-right-to-left-scan](v2-manual-right-to-left-scan/README.md) | Manual right-to-left scan | `O(n)` | `O(n)` | [▶ animation](v2-manual-right-to-left-scan/animation/index.html) |
