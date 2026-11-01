# 301. Remove Invalid Parentheses — v1: BFS by number of removals

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

## Approach: BFS by number of removals

> Level k of a BFS holds every string with k characters removed; the first level with a valid string is the answer.

**Breadth-first.** Start from `s`. Check every string on the current level; if any are valid, return those. Otherwise build the next level
by deleting one parenthesis from each string, using a `MyHashSet` so each string is generated once.

* Time: **O(2ⁿ · n)** — in the worst case many subsets are explored, each checked in linear time.
* Space: **O(2ⁿ · n)** — the levels and the visited set.

Hash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), instead of `java.util.HashMap`.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0301/v1/RemoveInvalidParentheses.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0301/v1/RemoveInvalidParenthesesTest.java` | JUnit 6 tests |
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

* [v2-dfs-with-counted-removals](../v2-dfs-with-counted-removals/README.md): DFS with counted removals (`O(2ⁿ · n)` time, `O(n²)` space)
