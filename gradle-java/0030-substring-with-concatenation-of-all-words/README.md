# 30. Substring with Concatenation of All Words

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Sliding Window &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

## Problem

You are given a string `s` and an array `words` of strings that all have the **same length**. A *concatenated substring* is a
substring of `s` made of every word in `words` exactly once, in any order. Return the starting indices of all concatenated
substrings in `s`, in any order.

**Example 1**
```
Input:  s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
```

**Example 2**
```
Input:  s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
```

**Example 3**
```
Input:  s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
```

**Constraints**
* `1 <= s.length <= 10^4`, `1 <= words.length <= 5000`, `1 <= words[i].length <= 30`

## Solutions

Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-check-every-start](v1-check-every-start/README.md) | Check every start | `O(n·k·L)` | `O(k)` | [▶ animation](v1-check-every-start/animation/index.html) |
| [v2-word-step-sliding-window](v2-word-step-sliding-window/README.md) | Word-step sliding window | `O(n·L)` | `O(k)` | [▶ animation](v2-word-step-sliding-window/animation/index.html) |
