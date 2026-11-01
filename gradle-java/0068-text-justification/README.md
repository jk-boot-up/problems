# 68. Text Justification

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Array / String &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/text-justification/)

## Problem

Given `words` and a width `maxWidth`, format the text so that every line has exactly `maxWidth` characters and is fully justified.
* Pack as many words as fit on each line (greedy), with at least one space between words.
* Spread extra spaces as evenly as possible between words; if they don't divide evenly, the **left** gaps get more.
* The **last line**, and any line with a single word, is left-justified and padded with spaces on the right.

**Example**
```
Input:  words = ["This","is","an","example","of","text","justification."], maxWidth = 16
Output: ["This    is    an",
         "example  of text",
         "justification.  "]
```

**Constraints**
* `1 <= words.length <= 300`, `1 <= words[i].length <= 20`
* `words[i].length <= maxWidth <= 100`

## Solutions

The folder below is a self-contained Gradle project.
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

| Project | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1-greedy-line-packing](v1-greedy-line-packing/README.md) | Greedy line packing | `O(L)` | `O(maxWidth)` | [▶ animation](v1-greedy-line-packing/animation/index.html) |
