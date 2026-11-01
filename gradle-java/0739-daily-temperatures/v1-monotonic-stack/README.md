# 739. Daily Temperatures — v1: Monotonic stack

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/daily-temperatures/)

## Problem

For each day, return how many days you must wait for a **warmer** temperature (0 if none).

**Example**
```
[73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
```

**Constraints**
* `1 <= n <= 10^5`; `30 <= temperatures[i] <= 100`

## Approach: Monotonic stack

> A stack holds days still waiting for a warmer day; each new day resolves all colder days on the stack.

**Decreasing stack of indices.** For each day `i`, while today is warmer than the day on top of the stack, pop it and set
`answer[top] = i - top`. Then push `i`.

* Time: **O(n)** — each index is pushed and popped once.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0739/v1/DailyTemperatures.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0739/v1/DailyTemperaturesTest.java` | JUnit 6 tests |
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
