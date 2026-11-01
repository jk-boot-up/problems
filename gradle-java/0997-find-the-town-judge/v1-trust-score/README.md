# 997. Find the Town Judge — v1: Trust score

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Graph General &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/find-the-town-judge/)

## Problem

In a town of `n` people, `trust[i] = [a, b]` means `a` trusts `b`. The judge trusts nobody, is trusted by everybody else, and there is
exactly one such person if any. Return the judge's label, or `-1`.

**Example**
```
n = 2, trust = [[1,2]]             → 2
n = 3, trust = [[1,3],[2,3]]       → 3
n = 3, trust = [[1,3],[2,3],[3,1]] → -1
```

**Constraints**
* `1 <= n <= 1000`

## Approach: Trust score

> The judge is trusted by everyone else and trusts nobody: in-degree n − 1 and out-degree 0.

**Net trust score.** `score[b]++` for being trusted, `score[a]--` for trusting. Only the judge reaches `n - 1`.

* Time: **O(n + t)** — one pass over trust, one over people.
* Space: **O(n)** — the scores.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0997/v1/FindTheTownJudge.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0997/v1/FindTheTownJudgeTest.java` | JUnit 6 tests |
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
