# 65. Valid Number — v1: Single scan with flags

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Strings &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/valid-number/)

## Problem

Return `true` if `s` is a valid number: an integer or decimal (optional sign, digits with at most one dot and at least one digit), optionally
followed by `e`/`E` and an integer exponent (optional sign, at least one digit).

**Example**
```
valid:   "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "53.5e93"
invalid: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "."
```

**Constraints**
* `1 <= s.length <= 20`

## Approach: Single scan with flags

> One pass tracking what has been seen (digits, a dot, an exponent) and rejecting anything out of place.

**Flags.** Scan once with `digits`, `dot` and `exp` flags. A sign is allowed only at the start or right after `e`. A dot is allowed once
and never after `e`. `e` needs digits before it and resets `digits` so that digits must follow. Anything else is invalid. Valid iff
`digits` at the end.

* Time: **O(n)** — one pass.
* Space: **O(1)** — three flags.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0065/v1/ValidNumber.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0065/v1/ValidNumberTest.java` | JUnit 6 tests |
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
