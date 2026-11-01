# 649. Dota2 Senate — v1: Two queues by turn order

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Queue &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/dota2-senate/)

## Problem

Senators from parties `R` and `D` act in order, round after round. Each active senator bans one opponent from all future rounds. When only
one party has active senators, it wins. Return `"Radiant"` or `"Dire"`.

**Example**
```
"RD" → "Radiant",   "RDD" → "Dire"
```

**Constraints**
* `1 <= n <= 10^4`

## Approach: Two queues by turn order

> Two queues of senator positions; the earlier senator bans the other and goes to the back of the line (index + n).

**Queues of turn indices.** Queue the positions of each party. Compare the fronts: the earlier one bans the other (who is dropped) and
re-enters its queue at `index + n`, i.e. in the next round.

* Time: **O(n)** — each ban removes one senator.
* Space: **O(n)** — the queues.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0649/v1/Dota2Senate.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0649/v1/Dota2SenateTest.java` | JUnit 6 tests |
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
