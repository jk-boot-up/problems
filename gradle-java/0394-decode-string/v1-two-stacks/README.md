# 394. Decode String — v1: Two stacks

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/decode-string/)

## Problem

Decode a string encoded as `k[encoded]`, meaning `encoded` repeated `k` times. Encodings may be nested; digits only appear as repeat counts.

**Example**
```
"3[a]2[bc]" → "aaabcbc",   "3[a2[c]]" → "accaccacc",   "2[abc]3[cd]ef" → "abcabccdcdcdef"
```

**Constraints**
* `1 <= s.length <= 30`; output length at most `10^5`.

## Approach: Two stacks

> On '[', save the current string and repeat count; on ']', repeat the inner string and append it to the saved one.

**Stacks of context.** Build the current string and current number. On `[`, push both and reset. On `]`, pop the outer string and count, and
set `current = outer + current × count`.

* Time: **O(output)** — every output character is written a constant number of times per nesting level.
* Space: **O(output)** — the builders and stacks.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0394/v1/DecodeString.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0394/v1/DecodeStringTest.java` | JUnit 6 tests |
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
