# 1431. Kids With the Greatest Number of Candies — v1: Compare with the maximum

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Arrays & Hashing &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

## Problem

For each kid, return whether giving them all `extraCandies` would make their count at least the largest count among all kids.

**Example**
```
candies = [2,3,5,1,3], extraCandies = 3 → [true,true,true,false,true]
```

**Constraints**
* `2 <= n <= 100`

## Approach: Compare with the maximum

> A kid can become (tied) greatest exactly when candies + extra reaches the current maximum.

**One maximum.** Compute `max`; kid `i` qualifies iff `candies[i] + extra >= max`.

* Time: **O(n)** — two passes.
* Space: **O(1)** — apart from the output.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1431/v1/KidsWithCandies.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1431/v1/KidsWithCandiesTest.java` | JUnit 6 tests |
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
