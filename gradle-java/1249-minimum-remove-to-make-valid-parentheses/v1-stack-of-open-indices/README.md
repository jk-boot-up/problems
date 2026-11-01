# 1249. Minimum Remove to Make Valid Parentheses — v1: Stack of open indices

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

## Problem

Remove the minimum number of parentheses from `s` (letters stay) so that the result is valid. Return any valid result.

**Example**
```
"lee(t(c)o)de)" → "lee(t(c)o)de"
"a)b(c)d"       → "ab(c)d"
"))(("          → ""
```

**Constraints**
* `1 <= s.length <= 10^5`

## Approach: Stack of open indices

> Unmatched ')' are found left to right; '(' still open at the end are unmatched too; delete exactly those.

**Mark the unmatched.** Scan left to right with a stack of indices of `'('`. A `')'` with an empty stack has no partner: mark it. Otherwise
pop its partner. Any `'('` left on the stack never closes: mark those. Each marked character must go and removing them suffices, so it is
minimal.

* Time: **O(n)**.
* Space: **O(n)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1249/v1/MinRemoveToMakeValid.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1249/v1/MinRemoveToMakeValidTest.java` | JUnit 6 tests |
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
