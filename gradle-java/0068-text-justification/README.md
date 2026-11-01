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

One solution, in subproject `v1`.

| Version | Approach | Time | Space | Animation |
|---------|----------|------|-------|-----------|
| [v1](v1/README.md) | Optimal | `O(L)` | `O(maxWidth)` | [▶ animation](v1/animation/index.html) |

## Build and test

Only a JDK is needed to start Gradle; JDK 25 is downloaded automatically if it is missing.

```bash
./gradlew test          # every version
./gradlew :v1:test      # one version
```

## Animation

Open `vN/animation/index.html` in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech engine
  (untick *Narration* to mute). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves, and compared across versions.

Use the header to switch between Light, Medium and Dark themes and between solution versions.
