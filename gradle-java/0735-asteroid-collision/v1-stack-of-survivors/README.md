# 735. Asteroid Collision — v1: Stack of survivors

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Stack &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/asteroid-collision/)

## Problem

Each asteroid's size is `|a|` and its direction is its sign (`+` right, `-` left); all move at the same speed. When two meet, the smaller
explodes; equal sizes both explode. Return the asteroids left after all collisions.

**Example**
```
[5,10,-5] → [5,10],   [8,-8] → [],   [10,2,-5] → [10],   [-2,-1,1,2] → [-2,-1,1,2]
```

**Constraints**
* `2 <= n <= 10^4`; `a != 0`

## Approach: Stack of survivors

> A stack of surviving asteroids; a left-moving one collides with right-moving ones on top until it dies or none remain.

**Stack.** Right-movers just push. A left-mover fights the right-movers on top of the stack: it destroys smaller ones, dies against larger
ones, and both vanish on a tie. If it survives, push it.

* Time: **O(n)** — each asteroid is pushed and popped at most once.
* Space: **O(n)** — the stack.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0735/v1/AsteroidCollision.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0735/v1/AsteroidCollisionTest.java` | JUnit 6 tests |
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
