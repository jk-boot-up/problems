# 68. Text Justification — v1: Greedy line packing

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

## Approach: Greedy line packing

> Greedily pack words per line, then spread the spare spaces across gaps, giving the extra ones to the leftmost gaps.

**Greedy lines + space distribution.** Starting at word `i`, extend `j` while `lettersLength + (j - i) <= maxWidth`.
For a normal line with `gaps = j - i - 1`, total spaces = `maxWidth - letters`; each gap gets `spaces / gaps` and the first
`spaces % gaps` gaps get one more. The last line and single-word lines are joined with one space and right-padded.

* Time: **O(L)** — L is the total number of output characters (lines × maxWidth); each is written once.
* Space: **O(maxWidth)** — the builder for the current line, apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0068/v1/TextJustification.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0068/v1/TextJustificationTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
