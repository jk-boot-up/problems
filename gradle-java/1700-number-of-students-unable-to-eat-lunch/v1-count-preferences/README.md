# 1700. Number of Students Unable to Eat Lunch — v1: Count preferences

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Queue &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)

## Problem

Students in a queue each prefer circular (`0`) or square (`1`) sandwiches; sandwiches are in a stack (`sandwiches[0]` on top). The front
student takes the top sandwich if they like it, otherwise goes to the back of the queue. This stops when nobody in the queue wants the top
sandwich. Return how many students cannot eat.

**Example**
```
students = [1,1,0,0],     sandwiches = [0,1,0,1]     → 0
students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1] → 3
```

**Constraints**
* `1 <= n <= 100`

## Approach: Count preferences

> Queue order does not matter: the line only stalls when nobody left wants the sandwich on top.

**Counts suffice.** Students rotate freely, so the top sandwich is eventually taken if anyone still wants that type. Count students per
preference. For each sandwich from the top, if its count is zero, everyone left is stuck; otherwise decrement it.

* Time: **O(n)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1700/v1/StudentsUnableToEat.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1700/v1/StudentsUnableToEatTest.java` | JUnit 6 tests |
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
