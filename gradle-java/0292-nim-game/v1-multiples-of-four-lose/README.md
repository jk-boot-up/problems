# 292. Nim Game — v1: Multiples of four lose

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Math &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/nim-game/)

## Problem

There is a heap of `n` stones. Players alternate removing 1, 2 or 3 stones; whoever takes the last stone wins. You move first and both
players play optimally. Return `true` if you can win.

**Example**
```
n = 4 → false
n = 1 → true
n = 5 → true
```

**Constraints**
* `1 <= n <= 2^31 - 1`

## Approach: Multiples of four lose

> Multiples of 4 are losing positions: whatever you take, your opponent can make the total 4.

**Pattern.** With 1–3 stones you take them all. With 4, every move leaves 1–3 for your opponent. In general, if `n % 4 != 0` take
`n % 4` stones to leave a multiple of 4; from a multiple of 4, whatever `k` you take, the opponent takes `4 - k`.

* Time: **O(1)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0292/v1/NimGame.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0292/v1/NimGameTest.java` | JUnit 6 tests |
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
