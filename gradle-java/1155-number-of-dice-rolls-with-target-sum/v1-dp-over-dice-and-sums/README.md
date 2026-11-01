# 1155. Number of Dice Rolls With Target Sum — v1: DP over dice and sums

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Dynamic Programming &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)

## Problem

Roll `n` dice with `k` faces each (`1..k`). Return the number of ordered outcomes whose faces sum to `target`, modulo `10^9 + 7`.

**Example**
```
n = 1, k = 6, target = 3   → 1
n = 2, k = 6, target = 7   → 6
n = 30, k = 30, target = 500 → 222616187
```

**Constraints**
* `1 <= n, k <= 30`, `1 <= target <= 1000`

## Approach: DP over dice and sums

> ways[d][s] adds up ways[d − 1][s − f] over every face f of the last die.

**Last die.** With one fewer die, every sum `s - f` for a face `f` extends to `s`. Keep one row `ways[s]` for the dice so far and build the
next row from it. Reduce modulo `10^9 + 7` as you add.

* Time: **O(n · target · k)**.
* Space: **O(target)** — two rows.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p1155/v1/DiceRollsTargetSum.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p1155/v1/DiceRollsTargetSumTest.java` | JUnit 6 tests |
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
