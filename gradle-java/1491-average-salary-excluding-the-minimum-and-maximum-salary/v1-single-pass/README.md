# 1491. Average Salary Excluding the Minimum and Maximum Salary — v1: Single pass

**Difficulty:** Easy &nbsp;|&nbsp; **Topic:** Array &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/)

## Problem

Given unique salaries, return the average excluding the minimum and the maximum salary.

**Example**
```
[4000,3000,1000,2000] → 2500.0
[1000,2000,3000]      → 2000.0
```

**Constraints**
* `3 <= salary.length <= 100`

## Approach: Single pass

> One pass for the sum, the minimum and the maximum.

**Sum, min, max.** Add everything, then subtract the smallest and largest and divide by `n - 2`.

* Time: **O(n)**.
* Space: **O(1)**.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1491/v1/AverageSalary.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1491/v1/AverageSalaryTest.java` | JUnit 6 tests |
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
