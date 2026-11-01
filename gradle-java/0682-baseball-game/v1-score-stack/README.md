# 682. Baseball Game — v1: Score stack

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/baseball-game/)

## Problem

Process operations: an integer records that score; `"+"` records the sum of the previous two scores; `"D"` records double the previous score;
`"C"` removes the previous score. Return the sum of the remaining scores.

**Example**
```
["5","2","C","D","+"] → 30,   ["5","-2","4","C","D","9","+","+"] → 27
```

**Constraints**
* `1 <= operations.length <= 1000`

## Approach: Score stack

> A stack of valid scores: numbers push, '+' adds the top two, 'D' doubles the top, 'C' pops.

**Stack.** Apply each operation to a stack of scores, then sum the stack.

* Time: **O(n)** — O(1) per operation.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0682/v1/BaseballGame.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0682/v1/BaseballGameTest.java` | JUnit 6 tests |
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
