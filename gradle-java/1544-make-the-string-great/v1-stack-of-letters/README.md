# 1544. Make The String Great — v1: Stack of letters

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/make-the-string-great/)

## Problem

A string is **good** if no two adjacent characters are the same letter in different cases (like `"aA"`). Repeatedly remove such adjacent
pairs and return the resulting string (possibly empty).

**Example**
```
"leEeetcode" → "leetcode"
"abBAcC"     → ""
"s"          → "s"
```

**Constraints**
* `1 <= s.length <= 100`, English letters

## Approach: Stack of letters

> Use the output as a stack; drop the top whenever the next letter is the same letter in the other case.

**Stack.** Read characters left to right. If the next one and the top of the stack differ exactly by the case offset (`|a - b| == 32`),
pop; otherwise push. Removing a pair can expose a new pair, which the stack handles automatically.

* Time: **O(n)**.
* Space: **O(n)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1544/v1/MakeStringGreat.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1544/v1/MakeStringGreatTest.java` | JUnit 6 tests |
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
