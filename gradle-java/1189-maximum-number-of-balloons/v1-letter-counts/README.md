# 1189. Maximum Number of Balloons — v1: Letter counts

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/)

## Problem

Using each character of `text` at most once, how many times can you form the word `"balloon"`?

**Example**
```
"nlaebolko" → 1,   "loonbalxballpoon" → 2,   "leetcode" → 0
```

**Constraints**
* `1 <= text.length <= 10^4`

## Approach: Letter counts

> Count letters; the answer is limited by the scarcest letter of 'balloon' (l and o are needed twice).

**Bottleneck.** Count letters; the answer is `min(b, a, l/2, o/2, n)`.

* Time: **O(n)** — one counting pass.
* Space: **O(1)** — 26 counters.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1189/v1/MaximumBalloons.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1189/v1/MaximumBalloonsTest.java` | JUnit 6 tests |
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
