# 933. Number of Recent Calls — v1: Sliding queue

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Queue &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-recent-calls/)

## Problem

Implement `RecentCounter` with `ping(t)`: record a request at time `t` (strictly increasing) and return how many requests happened in the
inclusive range `[t - 3000, t]`.

**Example**
```
ping(1) → 1, ping(100) → 2, ping(3001) → 3, ping(3002) → 3
```

**Constraints**
* `1 <= t <= 10^9`; at most `10^4` calls.

## Approach: Sliding queue

> Keep pings in a queue and drop those older than t − 3000 from the front.

**Queue window.** Append `t`; pop from the front while the front is less than `t - 3000`; return the size.

* Time: **O(1)** — amortized per ping (each time is added and removed once).
* Space: **O(W)** — the pings within the last 3000 ms.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0933/v1/RecentCounter.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0933/v1/RecentCounterTest.java` | JUnit 6 tests |
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
