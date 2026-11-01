# 301. Remove Invalid Parentheses — v2: DFS with counted removals

**Difficulty:** Hard &nbsp;|&nbsp; **Topic:** Backtracking &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)

## Problem

Remove the **minimum** number of parentheses to make the string valid. Return every distinct valid result, in any order. Letters stay.

**Example**
```
"()())()"  → ["(())()","()()()"]
"(a)())()" → ["(a())()","(a)()()"]
")("       → [""]
```

**Constraints**
* `1 <= s.length <= 25`; `s` has letters and parentheses, at most 20 parentheses

## Approach: DFS with counted removals

> First count exactly how many '(' and ')' must go, then only explore removals of that many.

**Count, then prune.** One scan finds `open` (unmatched `(`) and `close` (unmatched `)`): exactly the minimum removals. Recurse, removing
one bracket at a time from `start` onward, only while the matching budget lasts. In a run of equal characters, only remove the first:
removing any of them yields the same string, so this avoids duplicate answers. When both budgets are 0, keep the string if it is valid.

* Time: **O(2ⁿ · n)** — subsets of removable brackets, each checked in linear time.
* Space: **O(n²)** — recursion depth times the copied strings.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0301/v2/RemoveInvalidParentheses.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0301/v2/RemoveInvalidParenthesesTest.java` | JUnit 6 tests |
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
* **Complexity:** time and space cost, plotted against the common growth curves, and compared with the other approaches.

Switch between Light, Medium and Dark themes in the header.

## Other approaches

* [v1-bfs-by-number-of-removals](../v1-bfs-by-number-of-removals/README.md): BFS by number of removals (`O(2ⁿ · n)` time, `O(2ⁿ · n)` space)
